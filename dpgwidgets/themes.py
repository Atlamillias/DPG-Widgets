from dpgwidgets.theme import Theme, Font



ImguiDark = Theme("ImguiDark").configure(
    color=dict(
        text=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        text_disabled=(0.50 * 255, 0.50 * 255, 0.50 * 255, 1.00 * 255),
        window_bg=(0.06 * 255, 0.06 * 255, 0.06 * 255, 0.94 * 255),
        child_bg=(0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255),
        popup_bg=(0.08 * 255, 0.08 * 255, 0.08 * 255, 0.94 * 255),
        border=(0.43 * 255, 0.43 * 255, 0.50 * 255, 0.50 * 255),
        border_shadow=(0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255),
        frame_bg=(0.16 * 255, 0.29 * 255, 0.48 * 255, 0.54 * 255),
        frame_bg_hovered=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255),
        frame_bg_active=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255),
        title_bg=(0.04 * 255, 0.04 * 255, 0.04 * 255, 1.00 * 255),
        title_bg_active=(0.16 * 255, 0.29 * 255, 0.48 * 255, 1.00 * 255),
        title_bg_collapsed=(0.00 * 255, 0.00 * 255, 0.00 * 255, 0.51 * 255),
        menu_bar_bg=(0.14 * 255, 0.14 * 255, 0.14 * 255, 1.00 * 255),
        scrollbar_bg=(0.02 * 255, 0.02 * 255, 0.02 * 255, 0.53 * 255),
        scrollbar_grab=(0.31 * 255, 0.31 * 255, 0.31 * 255, 1.00 * 255),
        scrollbar_grab_hovered=(0.41 * 255, 0.41 * 255,0.41 * 255, 1.00 * 255),
        scrollbar_grab_active=(0.51 * 255, 0.51 * 255, 0.51 * 255, 1.00 * 255),
        check_mark=(0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255),
        slider_grab=(0.24 * 255, 0.52 * 255, 0.88 * 255, 1.00 * 255),
        slider_grab_active=(0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255),
        button=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255),
        button_hovered=(0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255),
        button_active=(0.06 * 255, 0.53 * 255, 0.98 * 255, 1.00 * 255),
        header=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.31 * 255),
        header_hovered=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255),
        header_active=(0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255),
        separator=(0.43 * 255, 0.43 * 255, 0.50 * 255, 0.50 * 255),
        separator_hovered=(0.10 * 255, 0.40 * 255, 0.75 * 255, 0.78 * 255),
        separator_active=(0.10 * 255, 0.40 * 255, 0.75 * 255, 1.00 * 255),
        resize_grip=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.20 * 255),
        resize_grip_hovered=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255),
        resize_grip_active=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.95 * 255),
        tab=(0.18 * 255, 0.35 * 255, 0.58 * 255, 0.86 * 255),
        tab_hovered=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255),
        tab_active=(0.20 * 255, 0.41 * 255, 0.68 * 255, 1.00 * 255),
        tab_unfocused=(0.07 * 255, 0.10 * 255, 0.15 * 255, 0.97 * 255),
        tab_unfocused_active=(0.14 * 255, 0.26 * 255, 0.42 * 255, 1.00 * 255),
        docking_preview=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.70 * 255),
        docking_empty_bg=(0.20 * 255, 0.20 * 255, 0.20 * 255, 1.00 * 255),
        plot_lines=(0.61 * 255, 0.61 * 255, 0.61 * 255, 1.00 * 255),
        plot_lines_hovered=(1.00 * 255, 0.43 * 255, 0.35 * 255, 1.00 * 255),
        plot_histogram=(0.90 * 255, 0.70 * 255, 0.00 * 255, 1.00 * 255),
        plot_histogram_hovered=(1.00 * 255, 0.60 * 255,0.00 * 255, 1.00 * 255),
        table_header_bg=(0.19 * 255, 0.19 * 255, 0.20 * 255, 1.00 * 255),
        table_border_strong=(0.31 * 255, 0.31 * 255, 0.35 * 255, 1.00 * 255),
        table_border_light=(0.23 * 255, 0.23 * 255, 0.25 * 255, 1.00 * 255),
        table_row_bg=(0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255),
        table_row_bg_alt=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.06 * 255),
        text_selected_bg=(0.26 * 255, 0.59 * 255, 0.98 * 255, 0.35 * 255),
        drag_drop_target=(1.00 * 255, 1.00 * 255, 0.00 * 255, 0.90 * 255),
        nav_highlight=(0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255),
        nav_windowing_highlight=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.70 * 255),
        nav_windowing_dim_bg=(0.80 * 255, 0.80 * 255, 0.80 * 255, 0.20 * 255),
        modal_window_dim_bg=(0.80 * 255, 0.80 * 255, 0.80 * 255, 0.35 * 255),
        frame_bg=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.07 * 255),
        plot_bg=(0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255),
        plot_border=(0.43 * 255, 0.43 * 255, 0.50 * 255, 0.50 * 255),
        plot_legend_bg=(0.08 * 255, 0.08 * 255, 0.08 * 255, 0.94 * 255),
        plot_legend_border=(0.43 * 255, 0.43 * 255, 0.50 * 255, 0.50 * 255),
        plot_legend_text=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_title_text=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_inlay_text=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_x_axis=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_x_axis_grid=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.25 * 255),
        plot_y_axis=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_y_axis_grid=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.25 * 255),
        plot_y_axis2=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_y_axis_grid2=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.25 * 255),
        plot_y_axis3=(1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255),
        plot_y_axis_grid3=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.25 * 255),
        plot_selection=(1.00 * 255, 0.60 * 255, 0.00 * 255, 1.00 * 255),
        plot_query=(0.00 * 255, 1.00 * 255, 0.44 * 255, 1.00 * 255),
        plot_crosshairs=(1.00 * 255, 1.00 * 255, 1.00 * 255, 0.50 * 255),
        node_background=(50, 50, 50, 255),
        node_background_hovered=(75, 75, 75, 255),
        node_background_selected=(75, 75, 75, 255),
        node_outline=(100, 100, 100, 255),
        node_title_bar=(41, 74, 122, 255),
        node_title_bar_hovered=(66, 150, 250, 255),
        node_title_bar_selected=(66, 150, 250, 255),
        node_link=(61, 133, 224, 200),
        node_link_hovered=(66, 150, 250, 255),
        node_link_selected=(66, 150, 250, 255),
        node_pin=(53, 150, 250, 180),
        node_pin_hovered=(53, 150, 250, 255),
        node_box_selector=(61, 133, 224, 30),
        node_box_selector_outline=(61, 133, 224, 150),
        node_grid_background=(40, 40, 50, 200),
        node_grid_line=(200, 200, 200, 40),
    ),
    style=dict(
        alpha=None,
        button_text_align=None,
        cell_padding=None,
        child_border_size=None,
        child_rounding=None,
        frame_border_size=None,
        frame_padding=None,
        frame_rounding=None,
        grab_min_size=None,
        grab_rounding=None,
        indent_spacing=None,
        item_inner_spacing=None,
        item_spacing=None,
        popup_border_size=None,
        popup_rounding=None,
        scrollbar_rounding=None,
        scrollbar_size=None,
        selectable_text_align=None,
        tab_rounding=None,
        window_border_size=None,
        window_min_size=None,
        window_padding=None,
        window_rounding=None,
        window_title_align=None,
        plot_annotation_padding=None,
        plot_digital_bit_gap=None,
        plot_digital_bit_height=None,
        plot_error_bar_size=None,
        plot_error_bar_weight=None,
        plot_fill_alpha=None,
        plot_fit_padding=None,
        plot_label_padding=None,
        plot_legend_inner_padding=None,
        plot_legend_padding=None,
        plot_legend_spacing=None,
        plot_line_weight=None,
        plot_major_grid_size=None,
        plot_major_tick_len=None,
        plot_major_tick_size=None,
        plot_marker=None,
        plot_marker_size=None,
        plot_marker_weight=None,
        plot_minor_alpha=None,
        plot_minor_grid_size=None,
        plot_minor_tick_len=None,
        plot_minor_tick_size=None,
        plot_mouse_pos_padding=None,
        plot_border_size=None,
        plot_default_size=None,
        plot_min_size=None,
        plot_padding=None,
        node_grid_spacing=None,
        node_link_hover_distance=None,
        node_link_line_segments_per_length=None,
        node_link_thickness=None,
        node_border_thickness=None,
        node_corner_rounding=None,
        node_padding_horizontal=None,
        node_padding_vertical=None,
        node_pin_circle_radius=None,
        node_pin_hover_radius=None,
        node_pin_line_thickness=None,
        node_pin_offset=None,
        node_pin_quad_side_length=None,
        node_pin_triangle_side_length=None,
    ),
    font=dict(
        font=None,
        font_size=None
    )
)


DEFAULT = ImguiDark
