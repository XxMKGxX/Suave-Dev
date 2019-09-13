class ImportJournalEntryForm(BootstrapMixin, forms.Form):
    date = forms.DatField()
    memo = forms.CharField()
    file = forms.FileField()
    sheet_name = forms.CharField(max_length = 256)
    start_row = forms.IntegerField()
    end_row = forms.IntegerField()
    credit = forms.IntegerField()
    debit = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'date',
            'memo',
            'file',
            'sheet_name',
            'start_row',
            'end_row',
            'credit',
            'debit'
            )
        self.helper.add_input(Submit('submit', 'Submit'))

class ImportJournalEntryView(ContextMixin, FormView):
    form_class = forms.AccountingForm
    template_name = os.path.join('accounting','journal','import_entries.html')
    success_url = reverse_lazy('accounting:journal-list')

    extra_context = {
        'title': 'Journal Entry'
        }

    def form_valid(self, form):
        resp = super().form_valid(self)

        return render
