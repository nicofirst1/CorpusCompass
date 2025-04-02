# TODO: CURRENTLY NOT USED! Maybe delete this file, if DCThread class is used instead
import pandas as pd
from corpuscompass.model.files import File
from corpuscompass.model.variables_speakers import Variable, VariableValue, Speaker
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.corpus_compass_model import Project


class DatasetCreator:
    def __init__(self, project: "Project"):
        self.project: "Project" = project

    def create_main_dataset(
        self, ignore_unassigned_dv_values: bool = False
    ) -> pd.DataFrame:
        detected_speakers = self.project.get_detected_speakers()
        detected_annotations = self.project.get_detected_annotations()

        output_df = detected_annotations.loc[:, "token"]

        # Goal: Put each detected annotation in a separate column with the dependent variable name as a column name
        temp = detected_annotations.explode("identifier")
        # Get the dependent variable name for each annotation. If the annotation is not assigned to a DV, None is returned
        temp["variable"] = temp["identifier"].apply(
            lambda x: self.project.get_parent_name_of_dv_value(x)
        )
        temp["index"] = temp.index
        # Get annotations that are not assigned to a DV
        missing_variables = temp["variable"].isnull()

        # Pivot the table so that each DV has its own column
        annotations_with_dvs = temp.loc[
            ~missing_variables, ["identifier", "variable"]
        ].pivot(columns="variable")
        annotations_with_dvs = annotations_with_dvs.droplevel(0, axis=1)
        unassigned_annotations = (
            temp.loc[missing_variables, ["identifier", "index"]]
            .groupby("index")
            .apply(lambda x: x["identifier"].tolist(), include_groups=False)
        )

        # Add unassigned annotations to the output if wanted
        if not ignore_unassigned_dv_values:
            annotations_with_dvs["unassigned"] = unassigned_annotations

        # Add the annotations with DVs to the output
        output_df = pd.concat([output_df, annotations_with_dvs], axis=1)

        # Goal: Add the speaker information for each token to the output
        output_df["speaker"] = detected_annotations.apply(
            lambda x: self.project.get_speaker_from_text_position(
                x["file_name"], x["annotation_start"], x["annotation_end"]
            ),
            axis=1,
        )

        # Goal: Add the IV information for each speaker to the output
        temp = pd.DataFrame(index=detected_annotations.index)
        temp["variable_values"] = output_df["speaker"].apply(
            lambda x: self.project.get_iv_values_from_speaker(x)
        )
        temp = temp.explode("variable_values")
        temp["variables"] = temp["variable_values"].apply(
            lambda x: self.project.get_parent_name_of_iv_value(x)
        )
        ivs_with_values = temp.pivot(columns="variables")
        ivs_with_values = ivs_with_values.droplevel(0, axis=1)
        output_df = pd.concat([output_df, ivs_with_values], axis=1)

        # Add additional information like the file and the context of the annotation
        # output_df["context"] = detected_annotations.apply(lambda x: self.project.get_context_from_text_position(x["file_name"], x["annotation_start"], x["annotation_end"]), axis=1)
        output_df["file"] = detected_annotations.apply(
            lambda x: self.project.get_filepath_from_filename(x["file_name"]), axis=1
        )

        # output_df.to_csv("dataset.csv", encoding="utf-8", index=False, sep=";")

        return detected_annotations
