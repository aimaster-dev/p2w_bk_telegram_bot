from project_pay2world.config import ProjectConfig
from create_app import create_app
import json
from constants import CMS_LANGUAGE_JSON

app = create_app(ProjectConfig)

jdata1 = open(app.static_folder + '/pay2world/assets/LANGUAGE/cmsLanguage.json', 'r', encoding='utf8').read()
jdata1 = json.loads(jdata1)
jdatas1 = {}
index_dict1 = {}
for index, jd in enumerate(jdata1):
    index = 'l'+str(index)
    index_dict1[index] = len(jd.get('zh'))
    jdatas1[index] = jd
ddd1 = sorted(index_dict1.items(), key=lambda x: x[1], reverse=True)
for dv in ddd1:
    CMS_LANGUAGE_JSON.append(jdatas1.get(dv[0]))

@app.route('/demo')
def demo1():
    from flask import render_template
    return render_template('pay_money.html')

if __name__ == '__main__':
    import logging
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run('0.0.0.0', port=5030, debug = True)
