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

class MigrationTest(TestCase):

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

class BillTests(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.bill = BillTest.objects.create(description='description')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.ocbjects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_bill_create_view(self):
        resp = self.client.get('/accounting/bill-create')
        self.assertEqual(resp.status_code, 200)

    def test_get_bill_update_view(self):
        resp = self.client.get('/accounting/bill-update/1')
        self.assertEqual(resp.status_code, 200)

    def test_get_bill_list_view(self):
        resp = self.client.get('/accounting/bill-list')
        self.assertEqual(resp.status_code, 200)

    def test_get_bill_detail_view(self):
        resp = self.client.get('/accounting/bill-detail/1')
        self.assertEqual(resp.status_code, 200)

    def test_post_bill_create_view(self):
        resp = self.client.post('/accounting/bill-create', data={'data':urllib.parse.quote(json.dumps([{
                'description':'description',
                'ammount':1}]))
                })
        self.assertEqual(resp.status_code, 302)

    def test_post_bill_update_view(self):
        resp = self.client.post('/accounting/bill-update/1', data={'data':urllib.parse.quote(json.dumps([{
                'description':'description',
                'ammount':1}]))
                })
        self.assertEqual(resp.status_code, 302)

class BillModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUpTestData(cls):
        cls.email = Email.objects.create(address='tkandoro63@gmail.com')
        cls.bill = Bill.objects.create('amount'=1)

    def test_create_test_bill(self):
        obj = Bill.objects.create(
                 reference='reference'
            )
            self.assertIsInstance(obj, Bill)

class BillPaymentViewTests(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.bill_payment = BillPaymentTest.objects.create(memo='memo')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.ocbjects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_bill_payment_create_view(self):
        resp = self.client.get('/accounting/bill-payment-create')
        self.assertEqual(resp.status_code, 200)

class BulkAccountTests(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.bulkacc = BulkAccountTest.objects.create(data='data')
        cls.user = User.objects.create_user(username='test', password='123')\
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_bulk_account_create_view(self):
        resp = self.client.get('/accounting/bulk-account-create')
        self.assertEqual(resp.status_code, 200)

    def test_post_bulk_account_create_view(self):
        resp = self.client.post('/accounting/bulk-account-create', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'description':'description',
                'code':1,
                'type':'credit',
                'balance':123,
                'balance_sheet_category':'balance'}]))
                })
        self.assertEqual(resp.status_code, 302)

class CreateMultipleEntriesView(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.multipleentries = CreateMultipleEntries.objects.create(date='date')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_create_multiple_entries_view(self):
        resp = self.client.get('/accounting/create-multiple-entries')
        self.assertEqual(resp.status_code, 200)

    def test_post_create_multiple_entries_view(self):
        resp = self.client.post('/accounting/create-multiple-entries', data={'data':urllib.parse.quote(json.dumps([{
                'date':01/01/2001,
                'memo':'memo',
                'credit':1,
                'account':0,
                'debit':1}]))
                })
        self.assertEqual(resp.status_code, 302)

class CreateMultipleExpensesView(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.multipleexpenses = CreateMultipleExpenses.objects.create(date=01/01/2001)
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_create_multiple_expenses_view(self):
        resp = self.client.get('/accounting/create-multiple-expenses')
        self.assertEqual(resp.status_code, 200)

    def test_post_create_multiple_expenses_view(self):
        resp = self.client.post('/accounting/create-multiple-expenses', data={'data':urllib.parse.quote(json.dumps([{
                'data':'data',
                'date':01/01/2001,
                'description':'description',
                'amount':123,
                'category':'category'}]))
                })
        self.assertEqual(resp.status_code, 302)

class ImportExpensesView(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.importexpenses = ImportExpenses.objects.create(date=01/01/2001)
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_import_expenses_view(self):
        resp = self.client.get('/accounting/import-expenses-')
        self.assertEqual(resp.status_code, 200)

    def test_post_import_expenses_view(self):
        resp = self.client.post('/accounting/import-expenses', data={'data':urllib.parse.quote(json.dumps([{
                'date':01/01/2001,
                'description':'description',
                'amount':123,
                'category':'category'}]))
                })
        self.assertEqual(resp.status_code, 302)

class CreateMultipleCustomersView(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.multiplecustomers = CreateMultipleCustomers.objects.create(date=01/01/2001)
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_create_multiple_customers_view(self):
        resp = self.client.get('/invoicing/create-multiple-customers')
        self.assertEqual(resp.status_code, 200)

    def test_post_create_multiple_customers_view(self):
        resp = self.client.post('/invoicing/create-multiple-customers', data={'data':urllib.parse.quote(json.dumps([{
                'name':'name',
                'business_address':'address',
                'email':self.email.pk,
                'phone':123456}]))
                })
        self.assertEqual(resp.status_code, 302)

class ImportCustomersView(TestCase):

    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUpTestData(cls):
        cls.importcustomers = ImportCustomers.objects.create(name='name')
        cls.user = User.objects.create_user(username='test',password='123')
        cls.email = Email.objects.create(address='address')

    def setUp(self):
        self.client.login(username='test',password='123')

    def test_get_import_customers_view(self):
        resp = self.client.get('/invoicing/import-customers')
        self.assertEqual(resp.status_code, 200)

    def test_post_import_expenses_view(self):
        resp = self.client.post('/invoicing/import-customers', data={'data':urllib.parse.quote(json.dumps([{
                'name':1,
                'phone':123456,
                'address':2,
                'type':3,
                'email':self.email.pk,
                'account_balance':987654}]))
                })
        self.assertEqual(resp.status_code, 302)