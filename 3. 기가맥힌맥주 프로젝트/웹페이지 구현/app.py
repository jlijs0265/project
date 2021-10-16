from enum import auto
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components import Span
import plotly.express as px
from select_agol import Select as agol
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])

#레이아웃(떼서 이쁘게 하고싶었지만... 시간관계상...)
app.layout = html.Div(
[
    dbc.Row(dbc.Col(html.H1(children='맥주 추천 시스템'),style={'text-align':'center'})),
    
    dbc.Row(
        [
            dbc.Col(html.Div(children='즐겨 마신 맥주를 입력해주세요.'),style={'text-align':'center'}),
        ]
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(dcc.Input(id = 'beer-input', type = 'text'),width={'offset':5}),
            dbc.Col(html.Button('추천', id = 'input-button', n_clicks= 0),width=2),
        ],
    ),

    html.Br(),
    
    dbc.Row(
        [
        dbc.Col(html.Div(children='', id = 'beer-output'),style={'text-align':'center'}),
        ]
    ),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("", className="card-title",id = 'Beer-name-1'),
                            html.P([
                                "", ],
                                className="card-text", id = 'Beer-context-1'
                            ),
                        ],style={'text-align':'center'}
                    ),
                ],
                ),width=4,
            ),
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("", className="card-title",id = 'Beer-name-2'),
                            html.P([
                                "", ],
                                className="card-text", id = 'Beer-context-2'
                            ),
                        ],style={'text-align':'center'}
                    ),
                ],
                ),width=4
            ),
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4("", className="card-title",id = 'Beer-name-3'),
                            html.P([
                                "", ],
                                className="card-text", id = 'Beer-context-3'
                            ),
                        ],style={'text-align':'center'}
                    ),
                ],
                ),width=4
            ),
        ]
    ),
    html.Br(),

    dbc.Row(dbc.Col(html.H2(children='개발자 3인 추천 맥주'),style={'text-align':'center'})),

    html.Br(),


    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardImg(src='https://ifh.cc/g/0GXjmw.png', top=True, style={'width': '20rem','height':'20rem'}),
                    dbc.CardBody(
                        [
                            html.H4("Kronenbourg 1664 Blanc", className="card-title"),
                            html.P([html.Span("# 프랑스  # 과일향 Lover  # 한국 편의점 多",style={'color':'#e66a00','font-weight':'bold'})
                                ,html.Br(),html.Br(),
                                "- 상쾌한 오렌지향과 맛",html.Br(),
                                "- 자극이 적고, 약한 홉(Hop)맛",html.Br(),
                                "- 알코올 농도 5%" ],
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                ),#width=4
            ),

            dbc.Col(
                dbc.Card(
                [
                    dbc.CardImg(src='https://ifh.cc/g/aryWqK.jpg', top=True, style={'width': '20rem','height':'20rem'}),
                    
                    dbc.CardBody(
                        [
                            html.H4("Lower De Boom Barleywine", className="card-title"),
                            html.P([html.Span("# 미국식 크래프트 비어  # 달달한 쓴맛",style={'color':'#e66a00','font-weight':'bold'})
                                ,html.Br(),html.Br(),
                                '- 시트러스 감귤류 향기',html.Br(),
                                '- 초반엔 진득, 후반엔 홉(Hop)의 쓴맛',html.Br(),
                                '- 알코올 농도 11.5%'
                                ],
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                ),# width=4
            ),
            dbc.Col(
                dbc.Card(
                [
                    dbc.CardImg(src='https://ifh.cc/g/rjqkZ7.png', top=True, style={'width': '20rem','height':'20rem'}),
                    dbc.CardBody(
                        [
                            html.H4("Corona Extra", className="card-title"),
                            html.P([html.Span("# 멕시코 # 부드러운 페일라거",style={'color':'#e66a00','font-weight':'bold'}),html.Br(),html.Br(),
                                "- 깔끔하고 청량한 맛",html.Br(),
                                "- 약한 호피(Hoppy) & 몰티(Malty)",html.Br(),
                                "- 레몬, 라임을 곁들어 마시면 Good",html.Br(),
                                "- 알코올 농도 4.6%"],
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                ), #width=4
            ),
        ],style={'text-align':'center'}
    ),
    html.Br(),
   
])

@app.callback(
    dash.dependencies.Output('beer-output', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_beer(n_, beer_name):
    if n_ > 0:
        return ['입력하신 즐겨 마신 맥주는 {}입니다.'.format(beer_name), html.Br(),
            '아래는 추천하는 맥주 리스트 입니다.']
    else :
        return ''


@app.callback(
    dash.dependencies.Output('Beer-name-1', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_1(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        return ['2위', html.Br(),
                '{}'.format(cluster.select(cluster.find_cluster())[1])]
    else:
        return ''

@app.callback(
    dash.dependencies.Output('Beer-name-2', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_2(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        return ['1위',html.Br(),
                '{}'.format(cluster.select(cluster.find_cluster())[0])]
    else:
        return ''

@app.callback(
    dash.dependencies.Output('Beer-name-3', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_3(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        return ['3위',html.Br(),
                '{}'.format(cluster.select(cluster.find_cluster())[2])]
    else:
        return ''

@app.callback(
    dash.dependencies.Output('Beer-context-1', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_1(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        flavor_list = cluster.flavor(cluster.select(cluster.find_cluster())[1])
        rating = cluster.Rating(cluster.select(cluster.find_cluster())[1])
        food = cluster.Pairing_food(cluster.select(cluster.find_cluster())[1])
        return [html.Span('Rating : {:.2f}/5'.format(rating[0]),
                style={'color':'#e66a00','font-weight':'bold'}
                ),html.Br(),
                html.Br(),
                '맛의 비중', html.Br(),
                '{}'.format(flavor_list[0][0]),' : {:.2f}%'.format(flavor_list[0][1]), html.Br(),
                '{}'.format(flavor_list[1][0]),' : {:.2f}%'.format(flavor_list[1][1]), html.Br(),
                '{}'.format(flavor_list[2][0]),' : {:.2f}%'.format(flavor_list[2][1]), html.Br(),
                html.Br(),
                '같이 곁들여 먹으면 좋은 음식들',html.Br(),
                '{}'.format(food)]
    else:
        return ''

@app.callback(
    dash.dependencies.Output('Beer-context-2', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_2(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        flavor_list = cluster.flavor(cluster.select(cluster.find_cluster())[0])
        rating = cluster.Rating(cluster.select(cluster.find_cluster())[0])
        food = cluster.Pairing_food(cluster.select(cluster.find_cluster())[0])

        return [html.Span('Rating : {:.2f}/5'.format(rating[0]),
                style={'color':'#e66a00','font-weight':'bold'}
                ),html.Br(),
                html.Br(), 
                '맛의 비중', html.Br(),
                '{}'.format(flavor_list[0][0]),' : {:.2f}%'.format(flavor_list[0][1]), html.Br(),
                '{}'.format(flavor_list[1][0]),' : {:.2f}%'.format(flavor_list[1][1]), html.Br(),
                '{}'.format(flavor_list[2][0]),' : {:.2f}%'.format(flavor_list[2][1]), html.Br(),
                 html.Br(),
                '같이 곁들여 먹으면 좋은 음식들',html.Br(),
                '{}'.format(food)]
    else:
        return ''


@app.callback(
    dash.dependencies.Output('Beer-context-3', 'children'),
    dash.dependencies.Input('input-button','n_clicks'),
    dash.dependencies.State('beer-input','value'),
)
def update_recomend_beer_3(n_, beer_name):
    if n_ > 0:
        cluster = agol(beer_name)
        flavor_list = cluster.flavor(cluster.select(cluster.find_cluster())[2])
        rating = cluster.Rating(cluster.select(cluster.find_cluster())[2])
        food = cluster.Pairing_food(cluster.select(cluster.find_cluster())[2])

        return [html.Span('Rating : {:.2f}/5'.format(rating[0]),
                style={'color':'#e66a00','font-weight':'bold'}
                ),html.Br(),
                html.Br(), 
                '맛의 비중', html.Br(),
                '{}'.format(flavor_list[0][0]),' : {:.2f}%'.format(flavor_list[0][1]), html.Br(),
                '{}'.format(flavor_list[1][0]),' : {:.2f}%'.format(flavor_list[1][1]), html.Br(),
                '{}'.format(flavor_list[2][0]),' : {:.2f}%'.format(flavor_list[2][1]), html.Br(),
                 html.Br(),
                '같이 곁들여 먹으면 좋은 음식들',html.Br(),
                '{}'.format(food)]
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=False)