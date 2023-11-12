import pandas as pd
from django.db import connection
from bs4 import BeautifulSoup

def create_pivot(df):
    """
    Create a pivot table from a raw DataFrame and return it as a DataFrame
    """
    # 要设置为空的列
    columns_to_clear = ['task_name', 'scene_name']

    # 递归处理每一行，从第二行开始设置指定列的值为空
    for index, row in df.iloc[1:].iterrows():
        for col in columns_to_clear:
            df.at[index, col] = ''
        # 重新设置索引，从 1 开始自增
    df.index = range(1, len(df) + 1)
    df.rename(columns={'task_name': '任务', 'scene_name': '场景', 'si_name': '指标','score': '分数'}, inplace=True)
    return df

def make_score_editable(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')

    # 找到所有的tr元素
    for tr in soup.find_all('tr'):
        # 找到第四个td元素，并设置contenteditable属性为true
        td_elements = tr.find_all('td')
        if len(td_elements) >= 4:
            score_td = td_elements[3]
            score = int(score_td.get_text())
            score_td['contenteditable'] = 'true'

            # 根据分数添加相应的CSS类
            if score < 60:
                score_td['class'] = 'highlight-red'
            elif score >= 60:
                score_td['class'] = 'highlight-green'
            # 添加输入验证的JavaScript
            score_td['oninput'] = 'validateScoreInput(this)'
            score_td['onkeydown'] = 'validateKeyInput(event);'

            # 添加颜色高亮的JavaScript
            score_td['oninput'] += '; highlightScoreColor(this);'
            score_td['onkeydown'] += '; highlightScoreColor(this);'

            # 根据分数添加相应的CSS类
            if score < 60:
                score_td['class'] = ['highlight-red']
            elif score >= 60:
                score_td['class'] = ['highlight-green']


     # 添加验证函数的JavaScript代码
    validation_script = """
    <script>
        function validateScoreInput(element) {
            // 获取用户输入
            var input = element.innerText.trim();

            // 验证输入是否为数字
            var isNumeric = !isNaN(input);

            // 如果不是数字，清除输入
            if (!isNumeric) {
                element.innerText = '';
            }
        }

        function validateKeyInput(event) {
            // 检测回车和空格并阻止默认行为
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
            }
        }
    </script>
    """

    # 添加颜色高亮的JavaScript代码
    color_highlight_script = """
    <script>
        function highlightScoreColor(element) {
            // 获取分数
            var score = parseInt(element.innerText.trim());

            // 根据分数添加相应的CSS类
            if (score < 60) {
                element.classList.add('highlight-red');
                element.classList.remove('highlight-green');
            } else {
                element.classList.add('highlight-green');
                element.classList.remove('highlight-red');
            }
        }
    </script>
    """
    # 在 </table> 后插入验证函数的JavaScript代码
    table_tag = soup.find('table')
    if table_tag:
        table_tag.insert_after(BeautifulSoup(validation_script, 'html.parser'))
        table_tag.insert_after(BeautifulSoup(color_highlight_script, 'html.parser'))

    return str(soup)

def get_data_as_dataframe(task_id):
    # 执行查询获取数据
    with connection.cursor() as cursor:
        # 查询指标的类别
        query = f"""
                    SELECT task_name,scene_name,si_name
                    FROM task,scene,safety_indicator,task_operation,task_si
                    WHERE task_operation.task_id = {task_id}
                        AND task.scene_id = scene.scene_id
                        AND task_si.task_id = task.task_id
                        AND safety_indicator.si_id = task_si.si_id
                """
        cursor.execute(query)  # 直接使用表名执行查询
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    # 将数据转换为 DataFrame
    df = pd.DataFrame(data, columns=columns)
    # 对每个指标添加分数，默认60分
    df['score'] = 59

    with connection.cursor() as cursor:
        # 查询指标的类别
        query = f"""
                    SELECT user_name,task_create_time
                    FROM task,user
                    WHERE task.task_id = {task_id}
                        AND user.user_id = task.task_creator
                """
        cursor.execute(query)  # 直接使用表名执行查询
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    user_name, task_create_time = data[0]
    print(user_name,task_create_time)
    return df,user_name,task_create_time