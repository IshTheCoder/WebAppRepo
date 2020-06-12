import dash_bootstrap_components as dbc
import dash_html_components as html
def Navbar():
  """
  Returns navbard dash object
  """

  navbar = dbc.NavbarSimple(
         children=[
            dbc.Button(html.A('Home', href='/'), color='black'),
            dbc.Button(html.A('Page1', href='/page2'), color='black'),
            dbc.Button(html.A('Page2', href='/page4'), color='black'),
            dbc.Button(html.A("Page3", href="/page1"), color='black'),
            dbc.Button(html.A("Page4", href="/page3"), color='black'),
            dbc.Button(html.A("Page5", href="/page6"), color='black'),
            dbc.Button(html.A("Page6", href="/page5"), color='black'),
            dbc.DropdownMenu(
               nav=True,
               in_navbar=True,
               label="Menu",
               children=[
                  dbc.DropdownMenuItem(html.A('Page1', href='/page2')),
                  dbc.DropdownMenuItem(html.A('Page2', href='/page4')),
                  # dbc.DropdownMenuItem(divider=True),
                  dbc.DropdownMenuItem(html.A('Page3', href='/page1')),
                  dbc.DropdownMenuItem(html.A('Page4', href='/page3')),
                  dbc.DropdownMenuItem(html.A('Page5', href='/page6')),
                  dbc.DropdownMenuItem(html.A('Page6', href='/page5')),
                        ],
                    ),
                  ],
          # dbc.NavbarBrand
        brand="NBA",
        brand_href="/",
        sticky="top",
      )
  return navbar