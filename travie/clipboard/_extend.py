import clipboard
import time
import json
from functools import wraps
from typing import List, Any, Union, Dict, Generator
from travie.extend import ExtendCls

@ExtendCls(clipboard)
class __clipboard:
    @staticmethod
    def copy_lines(lines:"List[str]"):
        return clipboard.copy('\n'.join(lines))

    @staticmethod
    def paste_lines(strip=False,strip_lines=False, remove_blanks=False)->"List[str]":
        cv = clipboard.paste()
        if strip: cv = cv.strip()
        result = cv.splitlines()
        if strip_lines: result = [line.strip() for line in result]
        if remove_blanks: result = [line for line in result if line]
        return result

    @staticmethod
    @wraps(json.dumps,assigned=("__doc__", "__annotations__"))
    def copy_json(obj:"Any",**kwargs):
        import json
        return clipboard.copy( json.dumps(obj,**kwargs) )

    @staticmethod
    def paste_json()->"Union[Dict[str,Any],List[Any],str]":
        import json
        return json.loads( clipboard.paste() )

    @staticmethod
    def paste_gen(asjson=False, ignore_blank=True, ignore_whitespace=True, **kwargs)->"Generator[Union[str,dict,list],None,None]":
        cv = clipboard.paste()
        while True:
            while cv == (cv := clipboard.paste()):time.sleep(0.25)
            if ignore_blank and (cv.strip() if ignore_whitespace else cv) == "":continue
            yield (json.loads(cv,**kwargs) if asjson else cv)

    @staticmethod
    def paste_compile_single():
        exec(compile(clipboard.paste(),'__clipboard__', 'single'))
