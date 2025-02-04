from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Start date of the countdown (replace with the desired date)
LAUNCH_DATE = datetime(2025, 2, 4)

@app.route('/')
def index():
    now = datetime.now()
    # Number of days passed since LAUNCH_DATE
    days_passed = (now - LAUNCH_DATE).days + 1
    total_days = 365  # Font size will decrease to 0 in 365 days
    print(days_passed)
    # If accessed before the launch date, consider 0 days passed
    if days_passed < 0:
        days_passed = 0

    initial_size = 8  # Initial font size in vw

    # If 365 or more days have passed, the font size becomes 0
    if days_passed >= total_days:
        font_size = 0
    else:
        # Linear decrease of the font size
        font_size = initial_size * (1 - days_passed / total_days)

    # HTML template with Sawarabi Mincho font
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>The Story of the Famous Poet Nun</title>
      <!-- Include Japanese font from Google Fonts -->
      <link href="https://fonts.googleapis.com/css2?family=Sawarabi+Mincho&display=swap" rel="stylesheet">
      <style>
        body {
          background-color: white;
          margin: 0;
          padding: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
          font-family: 'Sawarabi Mincho', serif;
        }
        .text {
          font-size: {{ font_size }}vw;
          text-align: center;
        }
      </style>
    </head>
    <body>
      <div class="text">
        the story<br>
        of the famous poet nun
      </div>
    </body>
    </html>
    '''
    return render_template_string(template, font_size=font_size)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
