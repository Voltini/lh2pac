from dataclasses import dataclass
import pickle
import streamlit as st
import lh2pac.gemseo.discipline as discipline
import lh2pac.gemseo.utils as utils
import numpy as np


@dataclass
class InputVariable:
    display_name: str
    dict_name: str
    min_val: float
    max_val: float
    default_val: float


def draw_airplane(sliders: dict[str, float]):
    ac = discipline.H2TurboFan()
    ac.execute(sliders)
    fig = utils.draw_aircraft(
        ac, "Generated Aircraft", show=False
    ).get_figure()
    fig.set_size_inches(3, 3)
    logs = utils.get_aircraft_data(ac)
    return fig, logs


with open("optimums.pickle", "rb") as f:
    optimums_dict = pickle.load(f)

input_variables = [
    InputVariable("Thrust", "thrust", 1e5, 1.5e5, 1.25e5),
    InputVariable("Bypass ratio", "bpr", 5.0, 12.0, 8.5),
    InputVariable("Wing area", "area", 120.0, 200.0, 160.0),
    InputVariable("Wing aspect ratio", "aspect_ratio", 7.0, 12.0, 9.5),
]

st.set_page_config(layout="wide")

columns = st.columns([0.2, 0.8])

choice = columns[0].selectbox(
    "Load computed optimized parameters:",
    options=list(optimums_dict.keys()),
    index=None,
    placeholder="Select parameters to load."
)

sliders = {}
for input_var in input_variables:
    if not choice is None:
        print(optimums_dict[choice][input_var.dict_name])
    sliders[input_var.dict_name] = np.array(
        [
            (
                columns[0].slider(
                    input_var.display_name,
                    input_var.min_val,
                    input_var.max_val,
                    (
                        input_var.default_val
                        if choice is None
                        else optimums_dict[choice][input_var.dict_name][0]
                    ),
                )
            )
        ]
    )

draw_button = columns[0].button("Draw aircraft")

if draw_button:
    fig, logs = draw_airplane(sliders)
    result_column = columns[1].columns(2)
    result_column[0].pyplot(fig, use_container_width=False)
    result_column[1].code(logs)
