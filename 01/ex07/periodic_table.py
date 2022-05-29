def parse_elem(line):
    splited_line = line.split('=')
    elem = dict(values.strip().split(':') for values in splited_line[1].split(', '))
    elem["name"] = splited_line[0].strip()
    return elem


def parse_table():
    file = open('periodic_table.txt', 'r')
    table = [(parse_elem(line)) for line in file.readlines()]
    file.close()
    return table


def create_table_str():
    html_text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>periodic_table</title>
      <style>
        table {{
          border-collapse: collapse;
        }}
        h4 {{
          text-align: center;
        }}
        ul {{
          list-style:none;
          padding-left:0px;
        }}
      </style>
    </head>
    <body>
      <table>
        {body}
      </table>
    </body>
    </html>
        """
    one_element_text = """
            <td style="border: 1px solid black; padding:10px">
                <h4>{name}</h4>
                <ul>
                  <li>No {number}</li>
                  <li>{small}</li>
                  <li>{molar}</li>
                  <li>{electron} electron</li>
                </ul>
              </td>
        """

    table = parse_table()
    html_body = "<tr>"
    elem_position = 0
    for elem in table:
        if elem_position > int(elem["position"]):
            html_body += "    </tr>\n        <tr>"
            elem_position = 0
        for _ in range(elem_position, int(elem['position']) - 1):
            html_body += "            <td></td>\n"
        elem_position = int(elem['position'])
        html_body += one_element_text.format(name=elem['name'], number=elem['number'],
                                             small=elem['small'], molar=elem['molar'], electron=elem['electron'])
    html_body += "</tr>\n"

    html_str = html_text.format(body=html_body)
    return html_str


def write_table_to_html_file():
    file = open('periodic_table.html', 'w')
    file.write(create_table_str())
    file.close()


if __name__ == '__main__':
    write_table_to_html_file()
