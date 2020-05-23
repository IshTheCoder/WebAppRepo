import dash_bootstrap_components as dbc
import dash_html_components as html
def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.Button(html.A('Page1', href='/page1'),color='black'),
              dbc.Button(html.A('Page2', href='/page2'),color='black'),
              dbc.Button(html.A("Page3", href="/"),color='black'),
              dbc.Button(html.A("Page4", href="/"), color='black'),
              dbc.Button(html.A("Page5", href="/"), color='black'),
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
            # dbc.NavbarBrand
          brand="Home",
          brand_href="/page1",
          sticky="top",
        )
     return navbar