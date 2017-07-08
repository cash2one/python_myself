# -*- coding: utf-8 -*-
import traceback

def parse_decorator(return_type):
    """
    :param return_type: 用于捕捉页面解析的异常, 0表示返回数字0, 1表示返回空字符串, 2表示返回[],3表示返回False, 4表示返回{}, 5返回None
    :return: 0,'',[],False,{},None
    """

    def page_parse(func):
        # @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception:
                # print e
                print traceback.format_exc()

                if return_type == 5:
                    return None
                elif return_type == 4:
                    return {}
                elif return_type == 3:
                    return False
                elif return_type == 2:
                    return []
                elif return_type == 1:
                    return ''
                else:
                    return 0

        return handle_error

    return page_parse