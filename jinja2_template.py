from jinja2 import Template

def template_html_report(list,file_name):
    template = Template("""
    <style>
       table {
        width: 50%; 
        border-collapse: collapse;
       }
       td {
        border: 1px solid;
       }
      </style>
     <table>
        <tr>
        <th>Host Name</th>
        <th>Problems</th>
        <th>OK</th>
        {% for row in my_array %}
        </tr>
        <tbody>
        <tr>
            {% for item in row %}
            <td>{{item}}</td>
            {% endfor %}
        </tr>
        {% endfor %}
        </tbody>
    </table>""")
    html_jinja2 = template.render(my_array=list)

    with open(file_name + '.html', "w", encoding="utf-8") as file:
        file.write(html_jinja2)



