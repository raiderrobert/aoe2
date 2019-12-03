from starlette.applications import Starlette
from starlette.config import Config
from starlette.templating import Jinja2Templates 
from starlette.staticfiles import StaticFiles

from core.utils import make_mana, parse_mana

import pandas as pd
import numpy as np

config = Config(".env")

PREFERRED_URL_SCHEME = config('PREFERRED_URL_SCHEME', default='https')

templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.route('/')
async def homepage(request):
    url = 'https://docs.google.com/spreadsheet/pub?key=0Ahw-nN-YDuIEdHBzZ2R6Unl2eE9RaDNYUk5lUXdNRlE&single=true&gid=0&output=csv' 
    c = pd.read_csv(url) 
    c = c.replace(np.nan, '', regex=True)
    c['card_count'] = c['card_count'].apply(lambda x: int(x))
    c['mana'] = c.apply(make_mana, axis=1)
    c = c.loc[c['print']!=0]
    return templates.TemplateResponse('index.html', {'request':request, 'cards': c.to_dict(orient='records') })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
