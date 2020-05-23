import dash_bootstrap_components as dbc
import dash_html_components as html
def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              html.A('Page1', href='/page1'),
              html.A('Page2', href='/page2'),
              dbc.NavItem(dbc.NavLink("graph2", href="/page2/")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem("Entry 1"),
                    dbc.DropdownMenuItem("Entry 2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Entry 3"),
                          ],
                      ),
                    ],
          brand="Home",
          brand_href="/page1",
          sticky="top",
        )
     return navbar