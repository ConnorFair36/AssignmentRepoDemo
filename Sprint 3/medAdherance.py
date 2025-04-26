import menu_ui
import patient

if __name__ == "__main__":
    app = menu_ui.MainWindow()
    while(app.win_open):
        # app.update_idletasks()
        app.update()
        account = app.current_account()
        if(account != None):
            account.reminderCheck()
        