temp = 'openEdit(\'ff964328-97f6-4863-b70d-df0a322d44ce\',\'30\',\'\');return false;;PrimeFaces.ab({s:\'templateform:reFreshData:0:j_idt57\'});return false;'
re_str = r".*\((.*-.*-.*-.*-.*)?','"
import re
re_obj = re.match(re_str, temp)
new_temp = re_obj.group(1)
new_re_str = r"'(.*)','"
new_re_obj = re.match(new_re_str, new_temp)
print(new_re_obj.group(1))