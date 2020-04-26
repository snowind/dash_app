import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from layout.navbar import Navbar

nav = Navbar()
body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Heading"),
                     html.P(
                           "Content"
                           ),
                           dbc.Button("View details", color="secondary"),
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
                     html.H2("Graph"),
                     dcc.Graph(
                         figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def create_layout():
    layout = html.Div([
                 nav,
                 body
                ])
    return layout




