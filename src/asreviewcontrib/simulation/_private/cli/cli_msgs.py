def get_msg(model_type):
    return (
        f"Attempted reassignment of '{model_type}' model. Use the --force flag if you m"
        + "ean to overwrite the configuration from previous steps. "
    )


dont_reassign_bal_msg = get_msg("bal")
dont_reassign_clr_msg = get_msg("clr")
dont_reassign_fex_msg = get_msg("fex")
dont_reassign_ofn_msg = get_msg("ofn")
dont_reassign_qry_msg = get_msg("qry")
dont_reassign_sam_msg = get_msg("sam")
dont_reassign_stp_msg = get_msg("stp")
