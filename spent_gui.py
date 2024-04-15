
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang.builder import Builder
from spent import view , log, init,drop, create_budget_table, existing_tables,log_budgettable
from helpers import helper

    



class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty()
    manager = ObjectProperty()


class Inputscreen(Screen):
    pass 
class Tablescreen(Screen):

    def load_table(self):
        table_content = view()
        expense = str(table_content[0][0])
        table_content = table_content[1]
        layout = AnchorLayout()
        #mdlabel text
        self.ids.total_expense_id.text = expense
        
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.45, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            elevation = 20,
            use_pagination=True,
            column_data=[
                ("AMOUNT", dp(20)),
                ("CATEGORY", dp(20)),
                ("DATE", dp(20))],
            row_data=[ (f'{i[0]}', f'{i[1]}',f'{i[2]}')
                for i in table_content])
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()

class Budgetentryscreen(Screen):
    pass

class New_budget_entries(Screen):
    pass

sm = ScreenManager()


sm.add_widget(Inputscreen(name='screen1'))
sm.add_widget(Tablescreen(name='screen2'))
sm.add_widget(Budgetentryscreen(name='screen3'))
sm.add_widget(New_budget_entries(name='screen4'))



class EXPENSES(MDApp):
    def build(self):

        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Light'
        self.load = Builder.load_string(helper)
        
        return self.load
    
    def delete_data(self):
        drop()
    
    def show_data(self):
        self.expense_text = []
        self.expense_text.append(self.load.ids.screen_manager.get_screen('screen1').ids.expense_id.text)
        self.expense_text.append(self.load.ids.screen_manager.get_screen('screen1').ids.descriptioin_id.text)

        if  '' in self.expense_text :
            check_string = 'Please enter correctly'
            close_button = MDRectangleFlatButton (text ='close', on_release = self.close_dialog)
            self.dialog = MDDialog(title = 'Invalid Entry',text = check_string,size_hint = (0.7,1),buttons = [close_button])
            self.dialog.open()
        else:
             self.enter_expense()
            
    def check_data_screen4(self):
        self.expense_text = []
        self.expense_text.append(self.load.ids.screen_manager.get_screen('screen4').ids.budget_entry_id.text)
        self.expense_text.append(self.load.ids.screen_manager.get_screen('screen4').ids.description_budget_id.text)

        if  '' in self.expense_text :
            check_string = 'Please enter correctly'
            close_button = MDRectangleFlatButton (text ='close', on_release = self.close_dialog)
            self.dialog = MDDialog(title = 'Invalid Entry',text = check_string,size_hint = (0.7,1),buttons = [close_button])
            self.dialog.open()
        else:
             self.enter_buudget()

    def enter_buudget(self):
        budget_tablename = self.load.ids.screen_manager.get_screen('screen3').ids.budget_id.text
        expense_text = []
        expense_text.append(self.load.ids.screen_manager.get_screen('screen4').ids.budget_entry_id.text)
        expense_text.append(self.load.ids.screen_manager.get_screen('screen4').ids.description_budget_id.text)
        log_budgettable(budget_tablename,expense_text[0],expense_text[1])  
        print('entered')
        check_string = ''
        close_button = MDRectangleFlatButton (text ='Continue', on_release = self.close_dialog)
        self.dialog = MDDialog(title = 'EXPENSE ENTERED',text = check_string,size_hint = (0.7,1),buttons = [close_button])
        self.dialog.open()

    def wrong_budget_name(self):

        self.budget_name_text= self.load.ids.screen_manager.get_screen('screen3').ids.budget_id.text
        tables_name = existing_tables()

               
        if self.budget_name_text in tables_name:
    
            check_string = 'Table already exist'
            close_button = MDRectangleFlatButton (text ='close', on_release = self.close_dialog)
            self.dialog = MDDialog(title = 'Invalid Entry',text = check_string,size_hint = (0.7,1),buttons = [close_button])
            self.dialog.open()


        elif self.budget_name_text == '' or ',' in self.budget_name_text :
            check_string = 'Please enter correctly'
            close_button = MDRectangleFlatButton (text ='close', on_release = self.close_dialog)
            self.dialog = MDDialog(title = 'Invalid Entry',text = check_string,size_hint = (0.7,1),buttons = [close_button])
            self.dialog.open()
        else:
             self.create_budget_name(self.budget_name_text)
    
    def close_dialog(self,obj):
        self.dialog.dismiss()
    
    def enter_expense(self):
        expense_text = []
        expense_text.append(self.load.ids.screen_manager.get_screen('screen1').ids.expense_id.text)
        expense_text.append(self.load.ids.screen_manager.get_screen('screen1').ids.descriptioin_id.text)
        init()
        log(expense_text[0],expense_text[1])  
        check_string = ''
        close_button = MDRectangleFlatButton (text ='Continue', on_release = self.close_dialog)
        self.dialog = MDDialog(title = 'EXPENSE ENTERED',text = check_string,size_hint = (0.7,1),buttons = [close_button])
        self.dialog.open()
    
    def disable_others(self):
        print('entered here')
        if self.load.ids.screen_manager.get_screen('screen3').ids.but_1.disabled == False:
            self.load.ids.screen_manager.get_screen('screen3').ids.but_2.disabled = False
            print('Button One is now disabled. Button Two is now enabled.')
        else:
            print('Button One is now enabled. Button Two is now disabled.')

    
    
    def create_budget_name(self,budget_name_text):

        create_budget_table(budget_name_text)
        check_string = 'Press create table to enter data '
        close_button = MDRectangleFlatButton (text ='continue',on_release = self.close_dialog)
        self.dialog = MDDialog(title = 'Table Created',text = check_string,size_hint = (0.7,1),buttons = [close_button])
        self.dialog.open()
        self.disable_others() 
        print('hi')
    
    '''def dropdownmenu(self):
        
        self.dropdown = MDDropdownMenu

        self.dropdown.items.append(
            { 'table1' :'1',
            'table2':'2'}
        )'''

    '''def items(self):
        all_tables = existing_tables()
        for i in all_tables'''

       

    

EXPENSES().run()