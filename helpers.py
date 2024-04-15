helper= '''
MDNavigationLayout:
    id : navigate
    ScreenManager:
        Screen:
            MDTopAppBar:
                markup : True
                pos_hint:{'top':1}
                title:'[font=times]MENU[/font]'
                elevation:10
                left_action_items: [['menu',lambda x:nav_drawer.set_state('open')]]
            ScreenManager:
                id:screen_manager
                Inputscreen:
                Tablescreen:
                Budgetentryscreen:
                New_budget_entries:
                
     
            

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            manager:screen_manager
            nav_drawer:nav_drawer
        

<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineIconListItem:
                markup : True
                pos_hint:{'center_y':0.5}
                text:'[font=times]ADD EXPENSE[/font]'
                on_release:
                    root.nav_drawer.set_state('close')
                    root.manager.current = 'screen1'
                IconLeftWidget:
                    icon: 'wallet'
            OneLineIconListItem:
                markup : True
                text:'[font=times]EXPENSE TABLE[/font]'
                on_release:
                    root.nav_drawer.set_state('close')
                    root.manager.current = 'screen2'
                IconLeftWidget:
                    icon: 'file-table'
            OneLineIconListItem:
                markup : True
                text:'[font=times]Create New Budget[/font]'
                on_release:
                    root.nav_drawer.set_state('close')
                    root.manager.current = 'screen3'
                IconLeftWidget:
                    icon: 'file-table'

<Inputscreen>:
    name:'screen1'
    

    MDLabel:
        markup : True
        text : '[font=times]EXPENSE TRACKER[/font]'
        #mode : 'fill'
        halign : 'center'
        pos_hint : {'center_y':0.8}
        font_style:'H3'

    MDTextField:
        id: expense_id
        hint_text:'ENTER EXPENSE'
        helper_text:'Required'
        helper_text_mode:'on_error'
        icon_right:'wallet'
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        required:'True'
     
    MDTextField:
        id: descriptioin_id
        hint_text:'DESCRIPTION'
        helper_text:'Required'
        helper_text_mode:'on_error'
        icon_right:'wallet'
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        required:'True'
    
    MDRectangleFlatButton:
        markup : True
        text:'[font=times]ENTER[/font]'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press: app.show_data()

<Tablescreen>:
    name:'screen2'
    MDRectangleFlatButton:
        markup : True
        text:'[font=times]Delete Table[/font]'
        pos_hint:{'center_x':0.7,'center_y':0.1}
        on_press: app.delete_data()

    MDLabel:
        markup : True
        id:total_expense_id
        text : '[font=times]total expense[/font]'
        halign : 'center'
        pos_hint : {'center_y':0.8}
        font_style:'H4'
    
<Budgetentryscreen>:
    name:'screen3'
    MDTextField:
        id: budget_id
        hint_text:'ENTER NAME'
        helper_text:'Required'
        helper_text_mode:'on_error'
        icon_right:'wallet'
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:200
        required:'True'
    MDRectangleFlatButton:
        id:but_1
        markup : True
        text:'[font=times]ENTER[/font]'
        disabled : False
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press: 
            app.wrong_budget_name()
            #if app.wrong_budget_name() == True:root.manager.current = 'screen4'
            #else:pass
            

    MDRectangleFlatButton:
        id:but_2
        markup : True
        text:'[font=times]Create Table[/font]'
        disabled : True
        pos_hint:{'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'screen4'


<New_budget_entries>:
    name:'screen4'
    MDTextField:
        id:budget_entry_id
        hint_text:'ENTER EXPENSE'
        helper_text:'Required'
        helper_text_mode:'on_error'
        icon_right:'wallet'
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:200
        required:'True'
     
    MDTextField:
        id: description_budget_id
        hint_text:'DESCRIPTION'
        helper_text:'Required'
        helper_text_mode:'on_error'
        icon_right:'wallet'
        icon_right_color:app.theme_cls.primary_color
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:200
        required:'True'
    
    MDRectangleFlatButton:
        markup : True
        text:'[font=times]ENTER[/font]'
        pos_hint:{'center_x':0.5,'center_y':0.4}
    


    







    


'''
