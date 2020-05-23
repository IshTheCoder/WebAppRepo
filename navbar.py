import dash_bootstrap_components as dbc
import dash_html_components as html
def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.Button(html.A('Page1', href='/page1')),
              dbc.Button(html.A('Page2', href='/page2')),
              dbc.Button(html.A("Page3", href="/")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem(html.A('Page1', href='/page1')),
                    dbc.DropdownMenuItem(html.A('Page2', href='/page2')),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem(html.A('Page3', href='/')),
                          ],
                      ),
                    ],
          brand="Home",
          brand_href="/page1",
          sticky="top",
        )
     return navbar