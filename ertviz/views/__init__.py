import dash_html_components as html
import dash_core_components as dcc
import webviz_core_components as wcc
from .paremeter_view import parameter_view
from .ensemble_selector_view import ensemble_selector_view
from .parallel_coordinates_view import parallel_coordinates_view


def parameter_selector_view(parent):
    return html.Div(
        children=[
            html.Div(
                className="ert-dropdown-container",
                children=[
                    html.Label("Search:", className="ert-label"),
                    dcc.Input(
                        id=parent.uuid("parameter-selector-filter"),
                        type="search",
                        placeholder="Substring...",
                        className="ert-dropdown",
                    ),
                ],
            ),
            wcc.Select(
                id=parent.uuid("parameter-selector-multi"),
                multi=True,
                size=10,
                persistence=True,
                persistence_type="session",
                className="ert-dropdown",
            ),
            dcc.Dropdown(
                id=parent.uuid("parameter-selector-dropdown"),
                className="ert-dropdown",
                multi=True,
                searchable=False,
            ),
            dcc.Store(id=parent.uuid("paremeter-selection-store")),
        ],
    )


def response_view(parent, index=0):
    return [
        html.H5("Response plots"),
        html.Div(
            className="ert-dropdown-container",
            children=[
                html.Label("Response", className="ert-label"),
                dcc.Dropdown(
                    id={"index": index, "type": parent.uuid("response-selector")},
                    className="ert-dropdown",
                ),
                dcc.Checklist(
                    id=parent.uuid("response-observations-check"),
                    options=[
                        {
                            "label": "Show only responses with observations",
                            "value": "obs",
                        },
                    ],
                    value=[],
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    className="ert-graph-options",
                    children=[
                        html.Label("Graph Type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["Function plot", "Statistics"]
                            ],
                            value="Function plot",
                            id={"index": index, "type": parent.uuid("plot-type")},
                        ),
                    ],
                ),
                dcc.Graph(
                    id={
                        "index": index,
                        "id": parent.uuid("response-graphic"),
                        "type": parent.uuid("graph"),
                    },
                    config={"responsive": True},
                    className="ert-graph",
                ),
            ],
            className="ert-graph-container",
        ),
    ]


def response_obs_view(parent):
    return [
        html.H5("Observation/Misfits plots"),
        html.Div(
            className="ert-dropdown-container",
            children=[
                html.Label("Response", className="ert-label"),
                dcc.Dropdown(
                    id=parent.uuid("response-selector"),
                    className="ert-dropdown",
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    className="ert-graph-options",
                    children=[
                        html.Label("Y-axis type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["linear", "log"]
                            ],
                            value="linear",
                            id=parent.uuid("yaxis-type"),
                        ),
                        html.Label("Misfits Type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["Univariate", "Summary"]
                            ],
                            value="Univariate",
                            id=parent.uuid("misfits-type"),
                        ),
                    ],
                ),
                dcc.Graph(
                    id={
                        "id": parent.uuid("response-graphic"),
                        "type": parent.uuid("graph"),
                    },
                    className="ert-graph",
                ),
            ],
            className="ert-graph-container",
        ),
    ]
