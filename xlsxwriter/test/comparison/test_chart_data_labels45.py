###############################################################################
#
# Tests for XlsxWriter.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright (c), 2013-2019, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparison_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('chart_data_labels45.xlsx')

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()
        chart = workbook.add_chart({'type': 'column'})

        chart.axis_ids = [70329856, 71246976]

        data = [
            [1, 2, 3, 4, 5],
            [2, 4, 6, 8, 10],
            [3, 6, 9, 12, 15],
            [10, 20, 30, 40, 50],

        ]

        worksheet.write_column('A1', data[0])
        worksheet.write_column('B1', data[1])
        worksheet.write_column('C1', data[2])
        worksheet.write_column('D1', data[3])

        chart.add_series({
            'values': '=Sheet1!$A$1:$A$5',
            'data_labels': {'value': 1, 'custom': [{'value': '=Sheet1!$D$1', 'border': {'color': 'red'}, 'fill': {'color': '#00B050'}}]}
        })

        chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
        chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

        worksheet.insert_chart('E9', chart)

        workbook.close()

        self.assertExcelEqual()
