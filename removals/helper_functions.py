# Helper function: converts QuerySet from db to html table
def convert_query_to_html(query):
    html = """\
    <html>
      <body>"""
    if query.exists():
        for entry in query:
            html += f"""<div style="border:1px solid gray;border-radius:25px;padding:5px;margin-bottom:10px">
                         <h3>Date - {entry.date.strftime("%d/%m/%Y")}</h3>
                            <ul>
                              <li><strong>Time:</strong> {entry.time.strftime("%H:%M")}</li>
                              <li><strong>Name:</strong> {entry.name}</li>
                              <li><strong>Phone:</strong><a href="tel:{entry.phone}"> {entry.phone}</a></li>
                              <li><strong>Pickup:</strong> {entry.pickup}</li>
                              <li><strong>Delivery:</strong> {entry.delivery}</li>
                              <li><strong>Details:</strong> {entry.comment}</li>
                              <li><strong>Price:</strong> {entry.final_cost}</li>
                              <li><strong>Commission:</strong> {entry.commission}</li>
                             </ul>
                            </div>
                            """
    else:
        html += """<h2>No jobs for this date, mate!</h2>"""


    html += """</body>
               </html>"""

    return html