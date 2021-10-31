###############################################################################
#
# Tests for XlsxWriter.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright (c), 2013-2021, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparison_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('chartsheet07.xlsx')

        self.ignore_files = ['xl/printerSettings/printerSettings1.bin',
                             'xl/chartsheets/_rels/sheet1.xml.rels']
        self.ignore_elements = {'[Content_Types].xml': ['<Default Extension="bin"'],
                                'xl/chartsheets/sheet1.xml': ['<pageSetup', '<drawing']}

    def test_create_file(self):
        """Test the worksheet properties of an XlsxWriter chartsheet file."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()
        chartsheet = workbook.add_chartsheet()

        chart = workbook.add_chart({'type': 'bar'})

        chart.axis_ids = [61296640, 61298176]

        data = [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],

        ]

        worksheet.write_column('A1', data[0])
        worksheet.write_column('B1', data[1])
        worksheet.write_column('C1', data[2])

        chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
        chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
        chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

        chartsheet.set_paper(9)
        chartsheet.set_portrait()
        chartsheet.set_chart(chart)

        chartsheet.horizontal_dpi = 200
        chartsheet.vertical_dpi = 200

        workbook.close()

        self.assertExcelEqual()
