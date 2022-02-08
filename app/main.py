from typing import List
import xlsxwriter as xlsxwriter
from fastapi import Body, Response, FastAPI
import pdfkit as pdf
import pandas as pd
from fastapi.responses import StreamingResponse
import io
from pydantic import BaseModel

app = FastAPI()

class DataModelIn (BaseModel):
    json_input: List[dict] = []

@app.post("/convert_excel", response_description='xlsx')
async def convert_excel(data: DataModelIn = Body(...)):
    validate_input(data.json_input)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    column_count = 0
    for key in data.json_input[0].keys():
        worksheet.write(0, column_count, key)
        column_count += 1
    row_count = 1
    for row in data.json_input:
        column_iteration = 0
        for value in row.values():
            worksheet.write(row_count,column_iteration,value)
            column_iteration += 1
        row_count += 1
    workbook.close()
    output.seek(0)
    headers = {
        'Content-Disposition': 'attachment; filename="output.xlsx"'
    }
    return StreamingResponse(output, headers=headers)

@app.post("/convert_csv", response_description='csv')
async def convert_csv(data: DataModelIn = Body(...)):
    validate_input(data.json_input)
    df_values = pd.DataFrame(data.json_input)
    headers = {
        'Content-Disposition': 'attachment; filename="output.csv"'
    }
    return StreamingResponse(io.StringIO(df_values.to_csv(index=False)), media_type="text/csv",headers=headers)

@app.post("/convert_pdf", response_description='pdf')
async def convert_pdf(data: DataModelIn = Body(...)):
    validate_input(data.json_input)
    df_values = pd.DataFrame(data.json_input)
    headers = {
        'Content-Disposition': 'attachment; filename="output.pdf"'
    }
    return Response(content=pdf.from_string(df_values.to_html(index=False)), media_type="application/pdf", headers=headers)

async def validate_input (input):
    if len(input) <= 0:
        return {"error_message": f"No Data Found"}



