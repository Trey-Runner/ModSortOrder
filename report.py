import webbrowser

def make_html_report(sorted_mods):
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>RimWorld Mod Load Order</title>
    <style>
        body {
            background: #111827;
            color: white;
            font-family: Arial, sans-serif;
            padding: 30px;
        }

        h1 {
            color: #facc15;
        }

        .mod {
            background: #1f2937;
            margin: 10px 0;
            padding: 12px;
            border-radius: 8px;
            border-left: 5px solid #38bdf8;
        }

        .number {
            color: #facc15;
            font-weight: bold;
        }

        .id {
            color: #9ca3af;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>RimWorld Mod Load Order</h1>
"""

    for index, mod in enumerate(sorted_mods, start=1):
        html += """
    <div class="mod">
        <span class="number">""" + str(index) + """.</span>
        """ + mod["title"] + """
        <div class="id">Workshop ID: """ + mod["id"] + """</div>
    </div>
"""

    html += """
</body>
</html>
"""

    file = open("mod_load_order.html", "w", encoding="utf-8")
    file.write(html)
    file.close()

    webbrowser.open("mod_load_order.html")
