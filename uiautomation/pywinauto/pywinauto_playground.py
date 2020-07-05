from pywinauto.application import Application
import pywinauto

# start app
app = Application(backend='uia').start("notepad.exe")
print(app.is_process_running())

# app = Application(backend='uia').connect(process=12344)
# app = Application(backend='uia').connect(handle=)
# app = Application(backend='uia').connect(path="notepad.exe")
# app = Application(backend='uia').connect(title_re='.* - 記事本$', class_name='Notepad')

# get window
dlg_spec = app.window(title_re='.* - 記事本$', class_name='Notepad')
# dlg_spec = app['未命名 - 記事本']
# dlg_spec = app.window(best_match='未命名 - 記事本')

# highlight this window
dlg_spec.draw_outline()

# write something
edit_spec = dlg_spec.child_window(title="文字編輯器", auto_id="15", control_type="Edit")
edit_spec.set_text('99999')
# dlg_spec.menu_select("編輯 -> 取代(R)...")

# get infos
# dlg_spec.print_control_identifiers()
# dlg_spec.dump_tree()
# dlg_spec.print_ctrl_ids()

# get child window and invoke
# about_menuitem_handel = dlg_spec.child_window(title="說明", control_type="MenuItem")
# file_dlg_spec = dlg_spec.child_window(title="檔案(F)", control_type="MenuItem")
# file_dlg_spec.wrapper_object().invoke()
dlg_spec.child_window(title_re="編輯", control_type="MenuItem").wrapper_object().invoke()

# action
# dlg_spec.menu_select("檔案(&F) -> 結束(&X)")
dlg_spec.menu_select("檔案 -> 結束")
# dlg_spec.menu_select("(&F) -> (&X)")

# dlg_spec.close()
