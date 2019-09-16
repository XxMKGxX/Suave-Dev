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

class MigrationsTest(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.bt = BulkTest.objects.create(name='name')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.ocbjects.create(address='address')
        cls.ii = ImportTest.objects.create(type='type')
        cls.is = SupplierTest.objects.create(phone='phone')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_bulk_create_view(self):
        resp = self.client.get('/inventory/bulk_create_item')
        self.assertEqual(resp.status_code, 200)

    def test_get_item_create_view(self):
        resp = self.client.get('/inventory/import_item')
        self.assertEqual(resp.status_code, 200)

    def test_get_suppliers_create_view(self):
        resp = self.client.get('/inventory/import_suppliers')
        self.assertEqual(resp.status_code, 200)

    def test_get_multiple_create_view(self):
        resp = self.client.get('/inventory/create_multiple_suppliers')
        self.asserEqual(resp.status_code, 200)

    def test_post_bulk_create_view(self):
        resp = self.client.post('/accounting/bulk_create_item', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'purchase_price':1,
                'warehouse':'warehouse',
                'quantity':10,
                'type':'product',}]))
                })
        self.assertEqual(resp.status_code, 302)

    def test_post_item_create_view(self):
        resp = self.client.post('/accounting/import_item', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'purchase_price':1,
                'sales_price':2,
                'quantity':10,
                'type':'product',
                'unit':'unit'}]))
                })
        self.assertEqual(resp.status_code, 302)

    def test_post_suppliers_view(self):
        resp = self.client.post('/accounting/import_suppliers', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'address':'address',
                'email':self.email.pk,
                'phone':123,
                'account_balance':1}]))
                })
        self.assertEqual(resp.status_code, 302)

    def test_post_multiple_create_view(self):
        resp = self.client.post('/accounting/create_multiple_suppliers', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'address':'address',
                'email':self.email.pk,
                'phone':123,
                'account_balance':1}]))
                })
        self.assertEqual(resp.status_code, 302)

class MigrationsTest(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.ia = AccountsTest.objects.create(name='name')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.ocbjects.create(address='address')


    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_ia_create_view(self):
        resp = self.client.get('/accounting/import_accounts')
        self.assertEqual(resp.status_code, 200)

    def test_get_ba_create_view(self):
        resp = self.client.get('/accounting/bulk_account')
        self.assertEqual(resp.status_code, 200)

    def test_post_ia_create_view(self):
        resp = self.client.post('/accounting/import_accounts', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'description':'description',
                'balance_sheet_category':'equity',
                'code':1,
                'type':'credit',
                'balance':123}]))
                })
        self.assertEqual(resp.status_code, 302)

    def test_post_ba_create_view(self):
        resp = self.client.post('/accounting/bulk_account', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'description':'description',
                'balance_sheet_category':'equity',
                'code':1,
                'type':'credit',
                'balance':123}]))
                })
        self.assertEqual(resp.status_code, 302)