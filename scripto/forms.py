from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ClientForm(forms.Form):
    ch = (
        ('01','SPACE'),
        ('02','TAB'),
        ('03','CAPITAL'),
        ('04','UNDER SCORE'),
        ('05','HYPHEN'),
    )

    split_ch = (
        (False, 'No'),
        (True, 'Yes')
    )

    file_url = forms.CharField()
    start_str = forms.CharField()
    end_str = forms.CharField()
    deliminator = forms.ChoiceField(choices=ch)
    input_column_name = forms.CharField()
    output_column_name = forms.CharField()
    common_data = forms.CharField()
    split_checkbox = forms.ChoiceField(choices=split_ch)


# class SampleForm(forms.Form):
#     ch = (
#         ('01','SPACE'),
#         ('02','TAB'),
#         ('03','CAPITAL'),
#         ('04','UNDER SCORE'),
#         ('05','HYPHEN'),
#     )
#
#     split_ch = (
#         (False, 'False'),
#         (True, 'True')
#     )
#
#     file_url = forms.CharField()
#     start_str = forms.CharField()
#     end_str = forms.CharField()
#     deliminator = forms.ChoiceField(choices=ch)
#     input_column_name = forms.CharField()
#     output_column_name = forms.CharField()
#     common_data = forms.CharField()
#     split_checkbox = forms.ChoiceField(choices=split_ch)