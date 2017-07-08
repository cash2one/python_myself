# -*- coding: utf8 -*-

# sx = "减肥减肥dddccd  "
#
# print str(sx.strip())[4:]

stringsx = '''

  <div class="xiaoqu_info">
            <label class="xiaoqu_main_label">楼栋总数</label>
            <span class="xiaoqu_main_info"></span>
          </div>
          <div>

'''

import re

xiaoqu_infosre = re.findall(r'(<div class="xiaoqu_info">.*<\/div>)', stringsx)
print len(xiaoqu_infosre)
print xiaoqu_infosre