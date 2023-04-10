# -*- coding: utf-8 -*-
"""
Annotate label test module.
"""
from tests.pyxform_test_case import PyxformTestCase
from pyxform import constants


class AnnotateLabelTest(PyxformTestCase):
    """Test annotate_label XLSForms."""

    def test_annotated_label(self):
        """Test annotated label."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__contains=["[Name: name]", "[Type: string]"],
            annotate=["type", "name"],
        )

    def test_not_annotated_label(self):
        """Test not to annotated label if there is no annotate argument."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__not_contains=["[Name: name]", "[Type: string]"],
        )

    def test_annotated_label_contains_newline(self):
        """Test annotated label contains newline."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__contains=["\n"],
            annotate=["type"],
        )

    def test_annotated_label_with_underscore_field_name(self):
        """Test annotated label with underscore field name."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |            |       |
            |        | type   | name       | label |
            |        | string | field_name | Name  |
            """,
            xml__contains=[r"[Name: field\_name]"],
            annotate=["type", "name"],
        )

    def test_annotated_label_with_underscore_label_name(self):
        """Test annotated label with underscore label name."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |            |             |
            |        | type   | name       | label       |
            |        | string | field_name | Label_name  |
            """,
            xml__contains=[r"<label>Label_name"],
            annotate=["all"],
        )

    def test_annotated_label_with_underscore_in_ref_in_label_name(self):
        """Test annotated label with underscore in item reference in label name."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |         |                    |
            |        | type    |   name  | label              |
            |        | integer | int_num | Number             |
            |        | string  | str_num | Name_of ${int_num} |
            """,
            xml__contains=[r"<label>Name_of $[int\_num]"],
            annotate=["all"],
        )

    def test_annotated_label_with_underscore_in_multiple_ref_in_label_name(self):
        """Test annotated label with underscore in multiple item reference in label name."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |           |                                       |
            |        | type    |   name    | label                                 |
            |        | integer | int_num_1 | Number 1                              |
            |        | integer | int_num_2 | Number 2                              |
            |        | string  | str_num   | Name_of ${int_num_1} and ${int_num_2} |
            """,
            xml__contains=[r"<label>Name_of $[int\_num\_1] and $[int\_num\_2]"],
            annotate=["all"],
        )

    def test_annotate_label__for_select_one(self):
        """Test annotated label for select one item."""
        self.assertPyxformXform(
            md="""
            | survey   |                     |      |       |
            |          | type                | name | label |
            |          | select_one choices1 | a    | A     |
            | choices  |                     |      |       |
            |          | list_name           | name | label |
            |          | choices1            | 1    | One   |
            |          | choices1            | 2    | Two   |
            """,
            xml__contains=[r"[Type: select\_one choices1]"],
            annotate=["type", "name"],
        )

    def test_annotate_label__for_select_multiple(self):
        """Test annotated label for select multiple item."""
        self.assertPyxformXform(
            md="""
            | survey   |                          |      |       |
            |          | type                     | name | label |
            |          | select_multiple choices1 | a    | A     |
            | choices  |                          |      |       |
            |          | list_name                | name | label |
            |          | choices1                 | 1    | One   |
            |          | choices1                 | 2    | Two   |
            """,
            xml__contains=[r"[Type: select\_multiple choices1]"],
            annotate=["type", "name"],
        )

    def test_annotate_label__for_select_one_from_file(self):
        """Test annotated label for select one from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                               |                        |                      |
            |          | type                          | name                   | label                |
            |          | select_one_from_file file.csv | select_one_from_file_1 | Select one from file |
            """,
            xml__contains=[r"[Type: select\_one\_from\_file file.csv]"],
            annotate=["all"],
        )

    def test_annotate_label__message_for_select_one_from_file(self):
        """Test annotated label message for select one from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                               |                        |                      |
            |          | type                          | name                   | label                |
            |          | select_one_from_file file.csv | select_one_from_file_1 | Select one from file |
            """,
            xml__contains=[constants.ANNOTATE_SELECT_ONE_FROM_FILE_MESSAGE],
            annotate=["all"],
        )

    def test_annotate_label__newline_for_select_one_from_file(self):
        """Test annotated label newline for select one from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                               |                        |                      |
            |          | type                          | name                   | label                |
            |          | select_one_from_file file.csv | select_one_from_file_1 | Select one from file |
            """,
            xml__contains=["&lt;br&gt;"],
            annotate=["all"],
        )

    def test_annotate_label__for_select_multiple_from_file(self):
        """Test annotated label for select multiple from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                                    |                             |                           |
            |          | type                               | name                        | label                     |
            |          | select_multiple_from_file file.csv | select_multiple_from_file_1 | Select multiple from file |
            """,
            xml__contains=[r"[Type: select\_multiple\_from\_file file.csv]"],
            annotate=["all"],
        )

    def test_annotate_label__message_for_select_multiple_from_file(self):
        """Test annotated label message for select multiple from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                                    |                             |                           |
            |          | type                               | name                        | label                     |
            |          | select_multiple_from_file file.csv | select_multiple_from_file_1 | Select multiple from file |
            """,
            xml__contains=[constants.ANNOTATE_SELECT_ONE_FROM_FILE_MESSAGE],
            annotate=["all"],
        )

    def test_annotate_label__newline_for_select_multiple_from_file(self):
        """Test annotated label newline for select multiple from file."""
        self.assertPyxformXform(
            md="""
            | survey   |                                    |                             |                           |
            |          | type                               | name                        | label                     |
            |          | select_multiple_from_file file.csv | select_multiple_from_file_1 | Select multiple from file |
            """,
            xml__contains=["&lt;br&gt;"],
            annotate=["all"],
        )

    def test_annotated_label__for_image(self):
        """Test annotated label for image."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |       |            |       |
            |        | type  | name       | label |
            |        | image | image_name | Image |
            """,
            xml__contains=[r"[Name: image\_name]", "[Type: image]"],
            annotate=["all"],
        )

    def test_annotated_label__for_audio(self):
        """Test annotated label for audio."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |       |            |       |
            |        | type  | name       | label |
            |        | audio | audio_name | audio |
            """,
            xml__contains=[r"[Name: audio\_name]", "[Type: audio]"],
            annotate=["all"],
        )

    def test_annotated_label__for_video(self):
        """Test annotated label for video."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |       |            |       |
            |        | type  | name       | label |
            |        | video | video_name | video |
            """,
            xml__contains=[r"[Name: video\_name]", "[Type: video]"],
            annotate=["all"],
        )

    def test_annotate_label__for_choices(self):
        """Test to annotated label for choices."""
        self.assertPyxformXform(
            md="""
            | survey   |                          |      |       |
            |          | type                     | name | label |
            |          | select_one choices1      | a    | A     |
            | choices  |                          |      |       |
            |          | list_name                | name | label |
            |          | choices1                 | 1    | One   |
            |          | choices1                 | 2    | Two   |
            """,
            xml__contains=["<label>One [1]</label>", "<value>1</value>"],
            annotate=["type", "name"],
        )

    def test_annotate_label__for_choices__with_underscore_in_label(self):
        """
        Test to annotated label for choices with underscore in label.
        Will not prepend the undercore with backslash
        """
        self.assertPyxformXform(
            md="""
            | survey   |                          |      |           |
            |          | type                     | name | label     |
            |          | select_one choices1      | a    | A         |
            | choices  |                          |      |           |
            |          | list_name                | name | label     |
            |          | choices1                 | 1    | Label_One |
            |          | choices1                 | 2_   | Two       |
            """,
            xml__contains=[r"<label>Label_One [1]</label>", r"<label>Two [2_]</label>"],
            annotate=["all"],
        )

    def test_annotate_label__for_choices__with_curly_bracket_in_label(self):
        """Test to annotated label for choices with curly bracket chars in label."""
        self.assertPyxformXform(
            md="""
            | survey   |                          |      |             |
            |          | type                     | name | label       |
            |          | select_one choices1      | a    | A           |
            | choices  |                          |      |             |
            |          | list_name                | name | label       |
            |          | choices1                 | 1    | Label {One} |
            |          | choices1                 | 2    | Two         |
            """,
            xml__contains=[r"<label>Label [One] [1]</label>"],
            annotate=["all"],
        )

    def test_annotated_label__input_equals_all(self):
        """Test annotated label with input equals "all"."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__contains=["[Name: name]", "[Type: string]"],
            annotate=["all"],
        )

    def test_annotated_label__input_contains_all(self):
        """Test annotated label with input contains "all"."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__contains=["[Name: name]", "[Type: string]"],
            annotate=["type", "all"],
        )

    def test_annotated_label_with_curly_bracket_char_in_label(self):
        """Test annotated label with ["{", "}"] char in label."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |
            |        | type      | name       | label                                 | calculation |
            |        | string    | field_name | Event_1                               |             |
            |        | calculate | check1     |                                       | 1+1         |
            |        | calculate | check2     |                                       | 2+1         |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             |
            """,
            xml__contains=[r"<label>This is info: $[check1] / $[check2]"],
            annotate=["all"],
        )

    def test_annotated_label__body_class(self):
        """
        Test annotated label.
        Form body class always contains text-no-transform.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |
            |        | type   |   name   | label |
            |        | string |   name   | Name  |
            """,
            xml__contains=['<h:body class="no-text-transform">'],
            annotate=["all"],
        )

    def test_annotated_label__body_class_existing_style(self):
        """
        Test annotated label with existing style.
        Form body class always contains text-no-transform.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey   |        |          |       |
            |          | type   |   name   | label |
            |          | string |   name   | Name  |
            | settings |        |          |       |
            |          | style      |      |       |
            |          | theme-grid |      |       |
            """,
            xml__contains=['<h:body class="theme-grid no-text-transform">'],
            annotate=["all"],
        )

    def test_annotated_label__body_class_existing_style_no_text_transform(self):
        """
        Test annotated label with no-text-transform in existing style.
        Form body class always contains text-no-transform.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey   |        |          |       |
            |          | type   |   name   | label |
            |          | string |   name   | Name  |
            | settings |        |          |       |
            |          | style                     |     |       |
            |          | pages no-text-transform   |     |       |
            """,
            xml__contains=['<h:body class="pages no-text-transform">'],
            annotate=["all"],
        )

    def test_annotated_label__group_appearance(self):
        """
        Test annotated label.
        Group appearance class always contains no-collapse.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |             |         |         |
            |        | type        | name    | label   |
            |        | string      | name    | Name    |
            |        | begin group | group1  | Group 1 |
            |        | string      | address | Address |
            |        | end group   |         |         |
            """,
            xml__contains=['<group appearance="no-collapse" ref="/data/group1">'],
            annotate=["all"],
        )

    def test_annotated_label__group_existing_appearance(self):
        """
        Test annotated label.
        Group appearance class always contains no-collapse.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |             |         |         |            |
            |        | type        | name    | label   | appearance |
            |        | string      | name    | Name    |            |
            |        | begin group | group1  | Group 1 | w5         |
            |        | string      | address | Address |            |
            |        | end group   |         |         |            |
            """,
            xml__contains=['<group appearance="w5 no-collapse" ref="/data/group1">'],
            annotate=["all"],
        )

    def test_annotated_label__group_existing_appearance_no_collapse(self):
        """
        Test annotated label.
        Group appearance class always contains no-collapse.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |             |         |         |                |
            |        | type        | name    | label   | appearance     |
            |        | string      | name    | Name    |                |
            |        | begin group | group1  | Group 1 | w4 no-collapse |
            |        | string      | address | Address |                |
            |        | end group   |         |         |                |
            """,
            xml__contains=['<group appearance="w4 no-collapse" ref="/data/group1">'],
            annotate=["all"],
        )

    def test_annotated_label__repeat_appearance(self):
        """
        Test annotated label.
        Repeat appearance class doesn't contains no-collapse.
        """
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |              |         |          |
            |        | type         | name    | label    |
            |        | string       | name    | Name     |
            |        | begin repeat | repeat1 | repeat 1 |
            |        | string       | address | Address  |
            |        | end repeat   |         |          |
            """,
            xml__contains=['<repeat nodeset="/data/repeat1">'],
            annotate=["all"],
        )

    def test_annotated_label__type_style(self):
        """Test annotated label style for item type."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |        |        |
            |        | type    | name   | label  |
            |        | string  | title  | Title: |
            """,
            xml__contains=[
                '&lt;span style="color: black"&gt; [Type: string]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__name_style(self):
        """Test annotated label style for item name."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |        |        |
            |        | type    | name   | label  |
            |        | string  | title  | Title: |
            """,
            xml__contains=[
                '&lt;span style="color: orangered"&gt; [Name: title]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__itemgroup(self):
        """Test annotated label for item with itemgroup."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |                    |
            |        | type   |   name   | label | bind::oc:itemgroup |
            |        | string |   name   | Name  | ItemGroup1         |
            """,
            xml__contains=["[Item Group: ItemGroup1]"],
            annotate=["all"],
        )

    def test_annotated_label__itemgroup_style(self):
        """Test annotated label style for item with itemgroup."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |          |       |                    |
            |        | type   |   name   | label | bind::oc:itemgroup |
            |        | string |   name   | Name  | ItemGroup1         |
            """,
            xml__contains=[
                '&lt;span style="color: blue"&gt; [Item Group: ItemGroup1]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__relevant(self):
        """Test annotated label for item with relevant check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |                   |
            |        | type      | name       | label                                 | calculation | relevant          |
            |        | string    | field_name | Event_1                               |             |                   |
            |        | calculate | check1     |                                       | 1+1         |                   |
            |        | calculate | check2     |                                       | 2+1         |                   |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 * 2 |
            """,
            xml__contains=["[Show When: $[check2] gt 1 \* 2]"],
            annotate=["all"],
        )

    def test_annotated_label__relevant_style(self):
        """Test annotated label style for item with relevant check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | relevant      |
            |        | string    | field_name | Event_1                               |             |               |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 |
            """,
            xml__contains=[
                '&lt;span style="color: green"&gt; [Show When: $[check2] gt 1]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__relevant_bind(self):
        """Test annotated label bind for item with relevant check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | relevant      |
            |        | string    | field_name | Event_1                               |             |               |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 |
            """,
            xml__not_contains=[
                '<bind nodeset="/data/info" readonly="true()" relevant=" /data/check2  &gt; 1" type="string"/>'
            ],
            annotate=["all"],
        )

    def test_annotated_label__required(self):
        """Test annotated label for item with required check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |                   |
            |        | type      | name       | label                                 | calculation | required          |
            |        | string    | field_name | Event_1                               |             |                   |
            |        | calculate | check1     |                                       | 1+1         |                   |
            |        | calculate | check2     |                                       | 2+1         |                   |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 * 3 |
            """,
            xml__contains=["[Required: $[check2] gt 1 \* 3]"],
            annotate=["all"],
        )

    def test_annotated_label__required_style(self):
        """Test annotated label style for item with required check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | required      |
            |        | string    | field_name | Event_1                               |             |               |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 |
            """,
            xml__contains=[
                '&lt;span style="color: red"&gt; [Required: $[check2] gt 1]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__constraint(self):
        """Test annotated label for item with constraint check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |                   |
            |        | type      | name       | label                                 | calculation | constraint        |
            |        | string    | field_name | Event_1                               |             |                   |
            |        | calculate | check1     |                                       | 1+1         |                   |
            |        | calculate | check2     |                                       | 2+1         |                   |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} > 1 * 4 |
            """,
            xml__contains=["[Constraint: $[check2] gt 1 \* 4]"],
            annotate=["all"],
        )

    def test_annotated_label__constraint_style(self):
        """Test annotated label style for item with constraint check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | constraint    |
            |        | string    | field_name | Event_1                               |             |               |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             | ${check2} < 1 |
            """,
            xml__contains=[
                '&lt;span style="color: magenta"&gt; [Constraint: $[check2] lt 1]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__default(self):
        """Test annotated label for item with default check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | default       |
            |        | string    | field_name | Event_1                               |             | default_name  |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             |               |
            """,
            xml__contains=["[Default: default\_name]"],
            annotate=["all"],
        )

    def test_annotated_label__default__instance_without_default_value_1(self):
        """Test instance of field with default name should not contains its default value"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | default       |
            |        | string    | field_name | Event_1                               |             | default_name  |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             |               |
            """,
            xml__not_contains=["<field_name>default_name</field_name>"],
            annotate=["all"],
        )

    def test_annotated_label__default__instance_without_default_value_2(self):
        """Test instance of field with default name should not contains its default value"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | default       |
            |        | string    | field_name | Event_1                               |             | default_name  |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             |               |
            """,
            xml__contains=["<field_name/>"],
            annotate=["all"],
        )

    def test_annotated_label__dynamic_default__no_setvalue(self):
        """Test no setvalue of field with dynamic default"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |            |             |             |          |
            |        | type    | name       | label       | calculation | default  |
            |        | date    | field_date | Event_1     |             | today()  |
            """,
            xml__not_contains=[
                '<setvalue event="odk-instance-first-load" ref="/data/field_date"'
            ],
            annotate=["all"],
        )

    def test_annotated_label__default_style(self):
        """Test annotated label style for item with default check."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                                       |             |               |
            |        | type      | name       | label                                 | calculation | default       |
            |        | string    | field_name | Event_1                               |             | default_name  |
            |        | calculate | check1     |                                       | 1+1         |               |
            |        | calculate | check2     |                                       | 2+1         |               |
            |        | note      | info       | This is info:  ${check1} / ${check2}  |             |               |
            """,
            xml__contains=[
                '&lt;span style="color: deepskyblue"&gt; [Default: default\_name]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__calculation(self):
        """Test annotated label for item with calculation"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |            |                       |                                                                                          |          |          |
            |        | type    | name       | label                 | calculation                                                                              | required | readonly |
            |        | date    | dob        | Date of birth:        |                                                                                          | yes      |          |
            |        | date    | date_visit | Date of visit:        |                                                                                          | yes      |          |
            |        | integer | age_visit  | Age at date of visit: | round((decimal-date-time(${date_visit}) - decimal-date-time(${dob})) div 365.25 - .5, 0) |          | yes      |
            """,
            xml__contains=[
                "[Calculation: round((decimal-date-time($[date\_visit]) - decimal-date-time($[dob])) div 365.25 - .5, 0)]"
            ],
            annotate=["all"],
        )

    def test_annotated_label__calculation_style(self):
        """Test annotated label style for item with calculation"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |            |                       |                                                                                          |          |          |
            |        | type    | name       | label                 | calculation                                                                              | required | readonly |
            |        | date    | dob        | Date of birth:        |                                                                                          | yes      |          |
            |        | date    | date_visit | Date of visit:        |                                                                                          | yes      |          |
            |        | integer | age_visit  | Age at date of visit: | round((decimal-date-time(${date_visit}) - decimal-date-time(${dob})) div 365.25 - .5, 0) |          | yes      |
            """,
            xml__contains=[
                '&lt;span style="color: maroon"&gt; [Calculation: round((decimal-date-time($[date\_visit]) - decimal-date-time($[dob])) div 365.25 - .5, 0)]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__calculation_bind(self):
        """Test annotated label bind for item with calculation"""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |         |            |                       |                                                                                          |          |          |
            |        | type    | name       | label                 | calculation                                                                              | required | readonly |
            |        | date    | dob        | Date of birth:        |                                                                                          | yes      |          |
            |        | date    | date_visit | Date of visit:        |                                                                                          | yes      |          |
            |        | integer | age_visit  | Age at date of visit: | round((decimal-date-time(${date_visit}) - decimal-date-time(${dob})) div 365.25 - .5, 0) |          | yes      |
            """,
            xml__contains=['<bind calculate="string(\'\')" nodeset="/data/age_visit"'],
            annotate=["all"],
        )

    def test_annotated_label__trigger(self):
        """Test annotated label for item with trigger."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |           |                   |             |
            |        | type      | name      | label             | trigger     |
            |        | integer   | resprate  | Respiratory Rate: |             |
            |        | integer   | pulse     | Pulse:            | ${resprate} |
            """,
            xml__contains=["[Trigger: $[resprate]]"],
            annotate=["all"],
        )

    def test_annotated_label__trigger_style(self):
        """Test annotated label style for item with trigger."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |           |                   |             |
            |        | type      | name      | label             | trigger     |
            |        | integer   | resprate  | Respiratory Rate: |             |
            |        | integer   | pulse     | Pulse:            | ${resprate} |
            """,
            xml__contains=[
                '&lt;span style="color: darkgreen"&gt; [Trigger: $[resprate]]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__readonly(self):
        """Test annotated label for readonly item."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                      |          |                                                                                          |               
            |        | type      | name       | label                | readonly | calculation                                                                              |
            |        | date      | dob        | Date of Birth:       |          |                                                                                          |
            |        | date      | date_visit | Date of Visit:       |          |                                                                                          |
            |        | integer   | age        | Age at Date of Visit | yes      | round((decimal-date-time(${date_visit}) - decimal-date-time(${dob})) div 365.25 - .5, 0) |
            """,
            xml__contains=["[Read-Only: yes]"],
            annotate=["all"],
        )

    def test_annotated_label__readonly_style(self):
        """Test annotated label style for readonly item."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |            |                      |          |                                                                                          |               
            |        | type      | name       | label                | readonly | calculation                                                                              |
            |        | date      | dob        | Date of Birth:       |          |                                                                                          |
            |        | date      | date_visit | Date of Visit:       |          |                                                                                          |
            |        | integer   | age        | Age at Date of Visit | yes      | round((decimal-date-time(${date_visit}) - decimal-date-time(${dob})) div 365.25 - .5, 0) |
            """,
            xml__contains=[
                '&lt;span style="color: chocolate"&gt; [Read-Only: yes]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__repeat_count(self):
        """Test annotated label for repeat item with repeat_count."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey   |                    |            |             |              |
            |          | type               | name       | label       | repeat_count |
            |          | begin repeat       | repeat_one | Repeat One: | 3            |
            |          | select_one ongoing | select_1   | Ongoing?:   |              |
            |          | end repeat         |            |             |              |
            | choices  |                    |            |             |
            |          | list_name          | name       | label       |
            |          | ongoing            | 1          | Yes         |
            |          | ongoing            | 2          | No          |
            """,
            xml__contains=["[Repeat Count: 3]"],
            annotate=["all"],
        )

    def test_annotated_label__repeat_count_style(self):
        """Test annotated label style for repeat item with repeat_count."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey   |                    |            |             |              |
            |          | type               | name       | label       | repeat_count |
            |          | begin repeat       | repeat_one | Repeat One: | 3            |
            |          | select_one ongoing | select_1   | Ongoing?:   |              |
            |          | end repeat         |            |             |              |
            | choices  |                    |            |             |
            |          | list_name          | name       | label       |
            |          | ongoing            | 1          | Yes         |
            |          | ongoing            | 2          | No          |
            """,
            xml__contains=[
                '&lt;span style="color: lime"&gt; [Repeat Count: 3]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label__external(self):
        """Test annotated label for item with external binding."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |               |                |                   |
            |        | type      | name          | label          | bind::oc:external |
            |        | text      | external_info | External info: | clinicaldata      |
            """,
            xml__contains=["[External: clinicaldata]"],
            annotate=["all"],
        )

    def test_annotated_label__external_style(self):
        """Test annotated label style for item with external binding."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |           |               |                |                   |
            |        | type      | name          | label          | bind::oc:external |
            |        | text      | external_info | External info: | clinicaldata      |
            """,
            xml__contains=[
                '&lt;span style="color: indigo"&gt; [External: clinicaldata]&lt;/span&gt;'
            ],
            annotate=["all"],
        )

    def test_annotated_label_identifier(self):
        """Test annotated label for item with identifier field."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |            |       |                         |
            |        | type   | name       | label | instance::oc:identifier |
            |        | string | field_name | Name  | fieldId                 |
            """,
            xml__contains=["[Identifier: fieldId]"],
            annotate=["all"],
        )

    def test_annotated_label_identifier_style(self):
        """Test annotated label style for item with identifier field."""
        self.assertPyxformXform(
            name="data",
            md="""
            | survey |        |            |       |                         |
            |        | type   | name       | label | instance::oc:identifier |
            |        | string | field_name | Name  | fieldId                 |
            """,
            xml__contains=[
                '&lt;span style="color: tomato"&gt; [Identifier: fieldId]&lt;/span&gt;'
            ],
            annotate=["all"],
        )
