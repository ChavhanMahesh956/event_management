import io
from openpyxl import Workbook
from odoo import api, fields, models
import base64
import xlwt


class EventReportWizard(models.TransientModel):
    _name = "wizard.excel"
    _description = "Excel Wizard"

    date_from = fields.Date(string="Start Date")
    date_to = fields.Date(string="Date End")
    
    
    
    def action_print_excel(self):
        # Search for all records in the sale.order model
        event_data = self.env["event.event"].search([])

        # Create the Excel workbook and worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Event Sheet', cell_overwrite_ok=True)

        # Write the report title
        title_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write_merge(0, 0, 0, 5, 'Event Sheet Report', title_style)

        # Write the headers for the quotation data
        header_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write(1, 0, 'Registration Date', header_style)
        worksheet.write(1, 1, 'Organizer Name', header_style)
        worksheet.write(1, 2, 'Attendee Name', header_style)
        worksheet.write(1, 3, 'Event Name', header_style)
        worksheet.write(1, 4, 'Registration State', header_style)

        # Write the quotation data
        row = 2
        for event in event_data:
            # worksheet.write(row, 0, event.registration_date)
            # worksheet.write(row, 1, event.name)
            # worksheet.write(row, 2, str(event.name))
            # worksheet.write(row, 3, event.amount_total)
            # worksheet.write(row, 4, event.state)
            row += 1
            

        # Save the report file
        report_file = io.BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Quotation_Sheet_Report.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.encodebytes(report_file.getvalue()),
            'res_model': self._name,
            'res_id': self.id
        }) 

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }

