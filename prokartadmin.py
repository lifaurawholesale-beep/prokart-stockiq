import streamlit as st
import pandas as pd
import numpy as np
import re
import io
import os
import traceback
import base64

# ============================================================
# PROKART INVENTORY INTELLIGENCE
# ============================================================

st.set_page_config(
    page_title="ProKart Inventory Intelligence",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM PROKART STYLE
# ============================================================

st.markdown("""
<style>
    /* ===== RIGHT SIDE BOTTOM IMAGE ===== */

.prokart-bottom-image {
    width: 100%;
    min-height: 900px;
    margin-top: 30px;
    padding: 0;
    border-radius: 22px;
    overflow: hidden;
}

.prokart-bottom-image img {
    width: 100%;
    height: 900px;
    object-fit: cover;
    object-position: center;
    display: block;
}

.prokart-bottom-image-text {
    color: #CBD5E1;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 8px;
}

  
    /* ===== HEADINGS ===== */
    h1, h2, h3 {
        color: white !important;
    }

    /* ===== NORMAL TEXT ===== */
    p, label, span {
        color: #E5E7EB;
    }

    /* ===== KPI CARDS ===== */
    .kpi-card {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    }

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background: #05182D !important;
    background-color: #05182D !important;
}

.main,
.main > div,
.block-container {
    background: transparent !important;
}

.block-container {
    max-width: 1500px !important;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}


/* ============================================================
   GLOBAL TEXT
   ============================================================ */

.stApp p,
.stApp label,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #FFFFFF !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #041326 0%,
        #082440 48%,
        #061A31 100%
    ) !important;

    background-color: #082440 !important;

    border-right: 1px solid #214968 !important;

    box-shadow:
        8px 0 30px rgba(0,0,0,0.30) !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5,
section[data-testid="stSidebar"] h6 {
    color: #FFFFFF !important;
}


/* ============================================================
   SIDEBAR TITLES
   ============================================================ */

.sidebar-section-title {
    background: linear-gradient(
        135deg,
        #0E2B49,
        #153E63
    ) !important;

    border: 1px solid #285477 !important;
    border-left: 4px solid #FF7A00 !important;

    border-radius: 12px !important;

    padding: 12px 14px !important;

    margin-top: 12px !important;
    margin-bottom: 14px !important;

    color: #FFFFFF !important;

    font-size: 16px !important;
    font-weight: 800 !important;
}

.forecast-settings-title {
    color: #FFFFFF !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    margin-bottom: 12px !important;
}


/* ============================================================
   FORECAST SELECTBOX
   ============================================================ */

section[data-testid="stSidebar"]
div[data-baseweb="select"] {
    width: 100% !important;
    background: transparent !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div {
    background: #082440 !important;
    background-color: #082440 !important;
    background-image: none !important;

    border: 2px solid #396583 !important;
    border-radius: 10px !important;

    min-height: 46px !important;

    box-shadow:
        inset 0 1px 2px rgba(255,255,255,0.03),
        0 4px 12px rgba(0,0,0,0.25) !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div > div {
    background: #082440 !important;
    background-color: #082440 !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"]
div[role="button"] {
    background: #082440 !important;
    background-color: #082440 !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"]
div[role="button"] span {
    color: #000000 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div span {
    color: #000000 !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"] svg {
    color: #FF963D !important;
    fill: #FF963D !important;
}

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div:hover {
    background: #0B2D4D !important;
    background-color: #0B2D4D !important;
    border-color: #FF7A00 !important;
}


/* ============================================================
   DROPDOWN POPUP
   ============================================================ */

div[data-baseweb="popover"] {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;

    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;

    overflow: hidden !important;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.30) !important;
}

div[data-baseweb="popover"] div {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
}

div[data-baseweb="popover"]
li[role="option"] {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;

    color: #000000 !important;

    font-size: 16px !important;
    font-weight: 800 !important;

    padding: 12px 15px !important;
}

div[data-baseweb="popover"]
li[role="option"] * {
    color: #000000 !important;
    font-weight: 800 !important;
}

div[data-baseweb="popover"]
li[role="option"]:hover {
    background: #FFF1E5 !important;
    background-color: #FFF1E5 !important;

    color: #000000 !important;
}

div[data-baseweb="popover"]
li[role="option"][aria-selected="true"] {
    background: #FFE4CC !important;
    background-color: #FFE4CC !important;

    color: #000000 !important;
    font-weight: 900 !important;

    border-left: 4px solid #FF7A00 !important;
}


/* ============================================================
   FILE UPLOADER
   ============================================================ */

section[data-testid="stSidebar"]
[data-testid="stFileUploader"] {
    background: #082440 !important;
    background-color: #082440 !important;

    border: 1px solid #396583 !important;
    border-radius: 14px !important;

    padding: 10px !important;
    margin-bottom: 16px !important;

    box-shadow:
        0 7px 20px rgba(0,0,0,0.25) !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploader"] > div {
    background: transparent !important;
}


/* ============================================================
   UPLOAD DROPZONE
   ============================================================ */

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] {
    background: #102F50 !important;
    background-color: #102F50 !important;

    border: 2px dashed #FF7A00 !important;
    border-radius: 12px !important;

    min-height: 110px !important;

    transition: all 0.25s ease !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"]:hover {
    background: #153B5E !important;
    border-color: #FF963D !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] > div {
    background: transparent !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] span,
section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] small,
section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] p {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"] svg {
    color: #FF7A00 !important;
    fill: #FF7A00 !important;
}


/* ============================================================
   BROWSE BUTTON
   ============================================================ */

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"]
button {
    background: #FF7A00 !important;
    background-color: #FF7A00 !important;

    color: #FFFFFF !important;

    border: none !important;
    border-radius: 9px !important;

    font-weight: 800 !important;

    padding: 8px 18px !important;

    transition: all 0.2s ease !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"]
button span {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderDropzone"]
button:hover {
    background: #FF963D !important;
    transform: translateY(-1px) !important;
}


/* ============================================================
   UPLOADED FILE
   ============================================================ */

section[data-testid="stSidebar"]
[data-testid="stFileUploaderFile"] {
    background: #102F50 !important;
    background-color: #102F50 !important;

    border: 1px solid #396583 !important;
    border-radius: 10px !important;

    padding: 8px !important;
    margin-top: 8px !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderFile"] span {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderFile"] svg {
    color: #FF963D !important;
    fill: #FF963D !important;
}

section[data-testid="stSidebar"]
[data-testid="stFileUploaderFile"] button {
    background: #173D60 !important;
    background-color: #173D60 !important;

    color: #FF963D !important;

    border: 1px solid #315D80 !important;
    border-radius: 7px !important;
}


/* ============================================================
   KPI CARDS
   ============================================================ */

.kpi-card {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;

    border-radius: 16px !important;

    padding: 20px !important;

    min-height: 125px !important;

    border: 1px solid #E1E7EF !important;

    box-shadow:
        0 5px 18px rgba(0,0,0,0.15) !important;

    position: relative !important;
    overflow: hidden !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease !important;
}

.kpi-card::before {
    content: "" !important;

    position: absolute !important;

    left: 0 !important;
    top: 0 !important;

    width: 100% !important;
    height: 3px !important;

    background: linear-gradient(
        90deg,
        #FF7A00,
        #FFAD66
    ) !important;
}

.kpi-card,
.kpi-card *,
.kpi-card p,
.kpi-card span,
.kpi-card div,
.kpi-card h1,
.kpi-card h2,
.kpi-card h3,
.kpi-card h4 {
    color: #000000 !important;
}

.kpi-title {
    color: #667085 !important;

    font-size: 13px !important;
    font-weight: 700 !important;
}

.kpi-value {
    color: #0B1F3A !important;

    font-size: 27px !important;
    font-weight: 850 !important;
}

.kpi-icon {
    background: #FFF3E8 !important;
    color: #000000 !important;

    border-radius: 9px !important;
    padding: 6px !important;
}

.kpi-card:hover {
    transform: translateY(-5px) !important;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.20) !important;
}


/* ============================================================
   MAIN TITLE
   ============================================================ */

.main-title {
    font-size: 36px !important;

    font-weight: 850 !important;

    color: #FFFFFF !important;

    letter-spacing: -0.7px !important;

    text-align: center !important;

    margin-bottom: 5px !important;
}

.main-title,
.main-title * {
    color: #FFFFFF !important;
}


/* ============================================================
   SUBTITLE
   ============================================================ */

.subtitle {
    color: #FFFFFF !important;

    font-size: 14px !important;

    font-weight: 700 !important;

    text-align: center !important;

    opacity: 1 !important;

    margin-bottom: 20px !important;
}

.subtitle * {
    color: #FFFFFF !important;
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-title,
.section-title *,
.business-overview,
.business-overview *,
.inventory-filters,
.inventory-filters *,
.sales-trend,
.sales-trend *,
.stock-health,
.stock-health *,
.inventory-intelligence,
.inventory-intelligence *,
.purchase-recommendations,
.purchase-recommendations *,
.inventory-alerts,
.inventory-alerts *,
.state-wise-sales,
.state-wise-sales *,
.city-wise-sales,
.city-wise-sales *,
.low-inventory,
.low-inventory *,
.product-detail,
.product-detail *,
.reports,
.reports * {
    color: #FFFFFF !important;

    font-weight: 800 !important;

    opacity: 1 !important;

    text-shadow: none !important;
}

.section-title {
    font-size: 21px !important;

    margin-top: 28px !important;
    margin-bottom: 12px !important;

    padding-left: 10px !important;

    border-left: 4px solid #FF7A00 !important;

    line-height: 1.4 !important;
}


/* ============================================================
   ALERT CARDS
   ============================================================ */

.alert-card {
    background: #FFFFFF !important;

    border-left: 5px solid #FF7A00 !important;

    border-radius: 11px !important;

    padding: 15px !important;

    margin-bottom: 9px !important;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.12) !important;
}

.alert-card * {
    color: #000000 !important;
}

.danger-card {
    background: #FFF8F8 !important;
    border-left-color: #DC3545 !important;
}

.warning-card {
    background: #FFFAF0 !important;
    border-left-color: #F59E0B !important;
}

.success-card {
    background: #F5FFF8 !important;
    border-left-color: #16A34A !important;
}


/* ============================================================
   DOWNLOAD BUTTON
   ============================================================ */

.stDownloadButton button {
    background: #FF7A00 !important;
    background-color: #FF7A00 !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 9px !important;

    font-weight: 800 !important;

    transition: all 0.2s ease !important;
}

.stDownloadButton button * {
    color: #FFFFFF !important;
}

.stDownloadButton button:hover {
    background: #FF963D !important;
    transform: translateY(-2px) !important;
}


/* ============================================================
   NORMAL BUTTON
   ============================================================ */

.stButton button {
    border-radius: 9px !important;

    font-weight: 700 !important;

    transition: all 0.2s ease !important;
}

.stButton button:hover {
    transform: translateY(-2px) !important;
}


/* ============================================================
   TEXT INPUT
   ============================================================ */

div[data-baseweb="input"] {
    border-radius: 9px !important;
}

div[data-baseweb="input"] input {
    background: #FFFFFF !important;

    color: #0B1F3A !important;

    border-radius: 9px !important;

    font-weight: 600 !important;
}

div[data-baseweb="input"] input::placeholder {
    color: #667085 !important;
}


/* ============================================================
   SLIDER
   ============================================================ */

section[data-testid="stSidebar"]
[data-testid="stSlider"] {
    background: #102F50 !important;

    background-color: #102F50 !important;

    border: 1px solid #315D80 !important;

    border-radius: 11px !important;

    padding: 11px 13px !important;

    margin-bottom: 12px !important;
}

section[data-testid="stSidebar"]
[data-testid="stSlider"] label {
    color: #FFFFFF !important;

    font-weight: 700 !important;
}


/* ============================================================
   TABS
   ============================================================ */

button[data-baseweb="tab"] {
    color: #C8D5E3 !important;

    font-weight: 650 !important;
}

button[data-baseweb="tab"]:hover {
    color: #FF7A00 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #FF7A00 !important;

    font-weight: 800 !important;

    border-bottom-color: #FF7A00 !important;
}


/* ============================================================
   DATAFRAME
   ============================================================ */

div[data-testid="stDataFrame"] {
    border-radius: 12px !important;

    border: 1px solid #315D80 !important;

    box-shadow:
        0 4px 14px rgba(0,0,0,0.15) !important;

    overflow: hidden !important;
}


/* ============================================================
   EXPANDER
   ============================================================ */

.streamlit-expanderHeader {
    background: #FFFFFF !important;

    color: #0B1F3A !important;

    border-radius: 10px !important;

    font-weight: 700 !important;
}

.streamlit-expanderHeader * {
    color: #0B1F3A !important;
}


/* ============================================================
   HEADER
   ============================================================ */

header[data-testid="stHeader"] {
    background: #05182D !important;
}


/* ============================================================
   HIDE SCROLLBAR
   ============================================================ */

/* Chrome, Edge, Safari */
::-webkit-scrollbar {
    width: 0px !important;
    height: 0px !important;
}

/* Firefox */
html {
    scrollbar-width: none !important;
}

/* Internet Explorer / old Edge */
html {
    -ms-overflow-style: none !important;
}

/* Streamlit main page */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    scrollbar-width: none !important;
}

/* Hide scrollbar but keep scrolling */
[data-testid="stAppViewContainer"]::-webkit-scrollbar,
[data-testid="stMain"]::-webkit-scrollbar,
[data-testid="stMainBlockContainer"]::-webkit-scrollbar {
    width: 0px !important;
    height: 0px !important;
}


/* ============================================================
   HIDE STREAMLIT FOOTER / MENU
   ============================================================ */

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 900px) {

    .main-title {
        font-size: 28px !important;
    }

    .subtitle {
        font-size: 12px !important;
    }

    .section-title {
        font-size: 19px !important;
    }

    .kpi-card {
        min-height: 110px !important;
        padding: 15px !important;
    }

}


/* ============================================================
   FINAL OVERRIDE
   ============================================================ */

.section-title,
.section-title * {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

.business-overview,
.business-overview * {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# COLUMN NAME CLEANING
# ============================================================

def clean_column_name(col):

    col = str(col).strip().lower()

    col = re.sub(r"[_\-]+", " ", col)

    col = re.sub(r"[^a-z0-9\s]", " ", col)

    col = re.sub(r"\s+", " ", col).strip()

    return col


def clean_dataframe_columns(df):

    df = df.copy()

    df.columns = [
        clean_column_name(c)
        for c in df.columns
    ]

    return df


# ============================================================
# FIND COLUMN
# ============================================================

def find_column(df, possible_names):

    columns = list(df.columns)

    possible_names = [
        clean_column_name(x)
        for x in possible_names
    ]

    # Exact match
    for name in possible_names:

        if name in columns:
            return name

    # Partial match
    for col in columns:

        for name in possible_names:

            if name in col:
                return col

    return None


# ============================================================
# READ UPLOADED FILE
# ============================================================
@st.cache_data(show_spinner=False)
def read_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None

    filename = uploaded_file.name.lower()

    # ========================================================
    # CSV
    # ========================================================

    if filename.endswith(".csv"):

        df = pd.read_csv(
            uploaded_file,
            low_memory=False
        )

        return clean_dataframe_columns(df)

    # ========================================================
    # EXCEL
    # ========================================================

    if filename.endswith((".xlsx", ".xls")):

        uploaded_file.seek(0)

        normal_df = pd.read_excel(
            uploaded_file
        )

        normal_df = clean_dataframe_columns(
            normal_df
        )

        item_id = find_column(
            normal_df,
            [
                "item id",
                "itemid",
                "product id",
                "sku",
                "asin",
                "product asin",
                "amazon asin"
            ]
        )

        if item_id:

            return normal_df

        uploaded_file.seek(0)

        raw = pd.read_excel(
            uploaded_file,
            header=None
        )

        header_row = None

        for i in range(
            min(20, len(raw))
        ):

            text = " ".join(
                str(x)
                for x in raw.iloc[i].tolist()
            )

            text = clean_column_name(text)

            if (
                "item id" in text
                or "itemid" in text
                or "product id" in text
                or "sku" in text
                or "asin" in text
                or "product asin" in text
                or "amazon asin" in text
            ):

                header_row = i
                break

        if header_row is not None:

            uploaded_file.seek(0)

            df = pd.read_excel(
                uploaded_file,
                header=header_row
            )

        else:

            df = normal_df

        df = df.dropna(
            axis=0,
            how="all"
        )

        df = df.dropna(
            axis=1,
            how="all"
        )

        return clean_dataframe_columns(df)

    raise ValueError(
        "Only CSV, XLS and XLSX files are supported."
    )


# ============================================================
# NUMBER CONVERSION
# ============================================================

def convert_number(series):

    text = series.astype(str).str.strip()

    # Accounting-style negatives, e.g. "(123)" -> -123
    is_negative = text.str.match(r"^\(.*\)$")

    text = (
        text
        .str.replace(r"[()]", "", regex=True)
        .str.replace(",", "", regex=False)
        .str.replace("₹", "", regex=False)
        .str.replace("%", "", regex=False)
        .str.replace("--", "0", regex=False)
        .str.strip()
    )

    values = pd.to_numeric(text, errors="coerce").fillna(0)

    values = values.where(~is_negative, -values.abs())

    return values


# ============================================================
# STANDARDIZE ITEM ID
# ============================================================

def standardize_item_id(series):

    return (
        series
        .astype(str)
        .str.strip()
        .str.upper()
        .str.replace(r"\.0$", "", regex=True)
        .replace(
            [
                "NAN",
                "NONE",
                "NULL",
                "NA",
                ""
            ],
            np.nan
        )
    )


# ============================================================
# DETECT INVENTORY COLUMNS
# ============================================================

def detect_inventory_columns(df):

    return {

        "item_id": find_column(
            df,
            [
                "item id",
                "itemid",
                "product id",
                "sku",
                "asin",
                "product asin",
                "amazon asin"
            ]
        ),

        "snapshot": find_column(
            df,
            [
                "snapshot day",
                "snapshot date",
                "snapshot_day",
                "inventory date"
            ]
        ),

        "item_name": find_column(
            df,
            [
                "item name",
                "product name",
                "product",
                "name",
                "item_name"
            ]
        ),

        "brand": find_column(
            df,
            [
                "merchant brand name",
                "merchant_brand_name",
                "brand name",
                "brand",
                "brand code"
            ]
        ),

        "warehouse": find_column(
            df,
            [
                "warehouse facility name",
                "warehouse",
                "facility name",
                "warehouse id",
                "warehouse_id"
            ]
        ),

        "inventory": find_column(
            df,
            [
                "sellable inventory units",
                "sellable_inventory_units",
                "total sellable",
                "sellable inventory",
                "current inventory",
                "available inventory",
                "stock",
                "inventory",
                "total inventory units",
                "total_inventory_units"
            ]
        ),

        "last_7": find_column(
            df,
            [
                "last 7 days",
                "last 7 day",
                "7 days",
                "last 7d",
                "7d sales",
                "sales 7d",
                "sales 7 days"
            ]
        ),

        "last_15": find_column(
            df,
            [
                "last 15 days",
                "last 15 day",
                "15 days",
                "last 15d",
                "15d sales",
                "sales 15d",
                "sales 15 days"
            ]
        ),

        "last_30": find_column(
            df,
            [
                "last 30 days",
                "last 30 day",
                "30 days",
                "last 30d",
                "30d sales",
                "sales 30d",
                "sales 30 days"
            ]
        )
    }


# ============================================================
# DETECT SALES COLUMNS
# ============================================================

def detect_sales_columns(df):

    return {

        "item_id": find_column(
            df,
            [
                "item id",
                "itemid",
                "product id",
                "sku",
                "asin",
                "product asin",
                "amazon asin"
            ]
        ),

        "date": find_column(
            df,
            [
                "order date",
                "order day",
                "order_day",
                "date",
                "order datetime",
                "transaction date"
            ]
        ),

        "order_id": find_column(
            df,
            [
                "order id",
                "order_id",
                "order number",
                "transaction id"
            ]
        ),

        "item_name": find_column(
            df,
            [
                "item name",
                "item_name",
                "product name",
                "product",
                "name"
            ]
        ),

        "brand": find_column(
            df,
            [
                "merchant brand name",
                "merchant_brand_name",
                "brand name",
                "brand",
                "brand code"
            ]
        ),

        "state": find_column(
            df,
            [
                "state",
                "state name"
            ]
        ),

        "city": find_column(
            df,
            [
                "city",
                "city name",
                "town"
            ]
        ),

        "pincode": find_column(
            df,
            [
                "pincode",
                "pin code",
                "postal code",
                "postal_code",
                "zip code",
                "zipcode"
            ]
        ),

        "quantity": find_column(
            df,
            [
                "quantity",
                "qty",
                "units",
                "sales quantity",
                "ordered quantity"
            ]
        ),

        "price": find_column(
            df,
            [
                "selling price",
                "unit price",
                "price"
            ]
        ),

        "amount": find_column(
            df,
            [
                "gross amount",
                "sales amount",
                "amount",
                "ordered product sales",
                "ordered_product_sales",
                "total sales"
            ]
        )
    }


# ============================================================
# PREPARE INVENTORY
# ============================================================

def prepare_inventory(df):

    detected = detect_inventory_columns(df)

    if detected["item_id"] is None:

        raise ValueError(
            "Inventory file does not contain Item ID / SKU / ASIN."
        )

    result = pd.DataFrame()

    # Item ID
    result["Item ID"] = standardize_item_id(
        df[detected["item_id"]]
    )

    # Item Name
    if detected["item_name"]:

        result["Item Name"] = (
            df[detected["item_name"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["Item Name"] = "Unknown"

    # Brand
    if detected["brand"]:

        result["Brand"] = (
            df[detected["brand"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["Brand"] = "Unknown"

    # Warehouse
    if detected["warehouse"]:

        result["Warehouse"] = (
            df[detected["warehouse"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["Warehouse"] = "Unknown"

    # Snapshot
    if detected["snapshot"]:

        result["Snapshot Date"] = pd.to_datetime(
            df[detected["snapshot"]],
            errors="coerce"
        )

    else:

        result["Snapshot Date"] = pd.NaT

    # Current Inventory
    if detected["inventory"]:

        result["Current Inventory"] = convert_number(
            df[detected["inventory"]]
        )

    else:

        result["Current Inventory"] = 0

    # Last 7
    if detected["last_7"]:

        result["Inventory Sales 7D"] = convert_number(
            df[detected["last_7"]]
        )

    else:

        result["Inventory Sales 7D"] = 0

    # Last 15
    if detected["last_15"]:

        result["Inventory Sales 15D"] = convert_number(
            df[detected["last_15"]]
        )

    else:

        result["Inventory Sales 15D"] = 0

    # Last 30
    if detected["last_30"]:

        result["Inventory Sales 30D"] = convert_number(
            df[detected["last_30"]]
        )

    else:

        result["Inventory Sales 30D"] = 0

    # Remove invalid IDs
    result = result[
        result["Item ID"].notna()
    ].copy()

    result = result.reset_index(drop=True)

    return result, detected


# ============================================================
# PREPARE SALES
# ============================================================

def prepare_sales(df):

    detected = detect_sales_columns(df)

    if detected["item_id"] is None:

        raise ValueError(
            "Sales file does not contain Item ID / SKU / ASIN."
        )

    result = pd.DataFrame()

    # ========================================================
    # ITEM ID
    # ========================================================

    result["Item ID"] = standardize_item_id(
        df[detected["item_id"]]
    )

    # ========================================================
    # ORDER DATE
    # ========================================================

    if detected["date"]:

        result["Order Date"] = pd.to_datetime(
            df[detected["date"]],
            errors="coerce"
        )

    else:

        result["Order Date"] = pd.NaT

    # ========================================================
    # ORDER ID
    # ========================================================

    if detected["order_id"]:

        result["Order ID"] = (
            df[detected["order_id"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["Order ID"] = np.nan

    # ========================================================
    # PRODUCT NAME
    # ========================================================

    if detected["item_name"]:

        result["Product Name"] = (
            df[detected["item_name"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["Product Name"] = "Unknown"

    # ========================================================
    # BRAND
    # ========================================================

    if detected["brand"]:

        result["Brand"] = (
            df[detected["brand"]]
            .astype(str)
            .str.strip()
        )

    else:
 
        result["Brand"] = "Unknown"

    # ========================================================
    # STATE
    # ========================================================

    if detected["state"]:

        result["State"] = (
            df[detected["state"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["State"] = "Unknown"

    # ========================================================
    # CITY
    # ========================================================

    if detected["city"]:

        result["City"] = (
            df[detected["city"]]
            .astype(str)
            .str.strip()
        )

    else:

        result["City"] = "Unknown"

    # ========================================================
    # PINCODE
    # ========================================================

    if detected["pincode"]:

        result["Pincode"] = (
            df[detected["pincode"]]
            .astype(str)
            .str.replace(r"\.0$", "", regex=True)
            .str.strip()
        )

    else:

        result["Pincode"] = "Unknown"

    # ========================================================
    # QUANTITY
    #
    # If Quantity does not exist:
    # every sales row = 1 unit
    # ========================================================

    if detected["quantity"]:

        result["Quantity"] = convert_number(
            df[detected["quantity"]]
        )

    else:

        result["Quantity"] = 1.0

    # ========================================================
    # SELLING PRICE
    # ========================================================

    if detected["price"]:

        result["Selling Price"] = convert_number(
            df[detected["price"]]
        )

    else:

        result["Selling Price"] = 0.0

    # ========================================================
    # SALES AMOUNT
    # ========================================================

    if detected["amount"]:

        result["Gross Amount"] = convert_number(
            df[detected["amount"]]
        )

    else:

        result["Gross Amount"] = (
            result["Quantity"]
            *
            result["Selling Price"]
        )

    # ========================================================
    # CLEAN INVALID IDS
    # ========================================================

    result = result[
        result["Item ID"].notna()
    ].copy()

    # ========================================================
    # CLEAN NUMBERS
    # ========================================================

    result["Quantity"] = (
        pd.to_numeric(
            result["Quantity"],
            errors="coerce"
        )
        .fillna(0)
        .clip(lower=0)
    )

    result["Gross Amount"] = (
        pd.to_numeric(
            result["Gross Amount"],
            errors="coerce"
        )
        .fillna(0)
        .clip(lower=0)
    )

    result = result.reset_index(drop=True)

    return result, detected


# ============================================================
# KPI CARD
# ============================================================

def kpi_card(icon, title, value):

    st.markdown(
        f"""
        <div class="kpi-card">
            <div>
                <span class="kpi-icon">{icon}</span>
                <span class="kpi-title">{title}</span>
            </div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FULL DATA PIPELINE (cached)
#
# Everything from reading the uploaded files through building
# the fully-computed "combined" table is wrapped in a single
# cached function. Without this, Streamlit re-runs the whole
# pipeline (including re-reading the Excel/CSV files) on every
# single widget interaction - typing in the search box, moving
# the safety-stock slider, picking a brand, etc. Caching keys
# on the file contents and the forecast settings, so it only
# recomputes when one of those actually changes.
# ============================================================

@st.cache_data(show_spinner="Processing Inventory and Sales data...")
def process_data(inventory_file, sales_file, future_days, safety_stock_percent):

    inventory_raw = read_uploaded_file(inventory_file)
    sales_raw = read_uploaded_file(sales_file)

    inventory, inventory_detected = prepare_inventory(inventory_raw)
    sales, sales_detected = prepare_sales(sales_raw)

    # ========================================================
    # LATEST INVENTORY SNAPSHOT
    #
    # Important:
    # If inventory file has many snapshot dates,
    # do NOT add stock from every historical snapshot.
    # Use the latest snapshot only.
    # ========================================================

    latest_snapshot = None

    if (
        "Snapshot Date" in inventory.columns
        and
        inventory["Snapshot Date"].notna().any()
    ):

        latest_snapshot = (
            inventory["Snapshot Date"]
            .dropna()
            .max()
        )

        inventory = inventory[
            inventory["Snapshot Date"] == latest_snapshot
        ].copy()

    # ========================================================
    # INVENTORY SUMMARY
    # ========================================================

    inventory_summary = (
        inventory
        .groupby(
            "Item ID",
            as_index=False
        )
        .agg({

            "Item Name": "first",

            "Brand": "first",

            "Current Inventory": "sum",

            "Inventory Sales 7D": "sum",

            "Inventory Sales 15D": "sum",

            "Inventory Sales 30D": "sum"
        })
    )

    # ========================================================
    # SALES SUMMARY
    # ========================================================

    sales_summary = (
        sales
        .groupby(
            "Item ID",
            as_index=False
        )
        .agg({

            "Product Name": "first",

            "Brand": "first",

            "Quantity": "sum",

            "Gross Amount": "sum"
        })
    )

    # ========================================================
    # MERGE
    # ========================================================

    combined = pd.merge(
        sales_summary,
        inventory_summary,
        on="Item ID",
        how="outer",
        suffixes=(
            "_Sales",
            "_Inventory"
        )
    )

    # ========================================================
    # CLEAN MERGED DATA
    # ========================================================

    combined["Product Name"] = (
        combined["Product Name"]
        .replace(
            ["nan", "None", "NAN"],
            np.nan
        )
    )

    combined["Item Name"] = (
        combined["Item Name"]
        .replace(
            ["nan", "None", "NAN"],
            np.nan
        )
    )

    combined["Product Name"] = (
        combined["Product Name"]
        .fillna(
            combined["Item Name"]
        )
        .fillna("Unknown")
    )

    combined["Brand"] = (
        combined["Brand_Sales"]
        .replace(
            ["nan", "None", "NAN"],
            np.nan
        )
        .fillna(
            combined["Brand_Inventory"]
        )
        .fillna("Unknown")
    )

    # ========================================================
    # NUMERIC FIELDS
    # ========================================================

    numeric_columns = [
        "Quantity",
        "Gross Amount",
        "Current Inventory",
        "Inventory Sales 7D",
        "Inventory Sales 15D",
        "Inventory Sales 30D"
    ]

    for col in numeric_columns:

        if col in combined.columns:

            combined[col] = (
                pd.to_numeric(
                    combined[col],
                    errors="coerce"
                )
                .fillna(0)
            )

    # ========================================================
    # HISTORICAL SALES PERIOD
    # ========================================================

    valid_dates = sales[
        sales["Order Date"].notna()
    ]["Order Date"]

    if len(valid_dates) > 0:

        min_date = valid_dates.min()

        max_date = valid_dates.max()

        history_days = (
            max_date - min_date
        ).days + 1

        history_days = max(
            history_days,
            1
        )

    else:

        history_days = 30

    # ========================================================
    # HISTORICAL DAILY DEMAND
    # ========================================================

    combined["Historical Daily Demand"] = np.where(

        history_days > 0,

        combined["Quantity"] / history_days,

        0
    )

    # ========================================================
    # 7 / 15 / 30 DAY DAILY DEMAND
    # ========================================================

    combined["Demand 7D"] = (
        combined["Inventory Sales 7D"] / 7
    )

    combined["Demand 15D"] = (
        combined["Inventory Sales 15D"] / 15
    )

    combined["Demand 30D"] = (
        combined["Inventory Sales 30D"] / 30
    )

    # ========================================================
    # SMART WEIGHTED DAILY DEMAND
    #
    # Recent demand gets more importance.
    #
    # 7D  = 50%
    # 15D = 30%
    # 30D = 20%
    # ========================================================

    weighted_demand = (

        combined["Demand 7D"] * 0.50

        +

        combined["Demand 15D"] * 0.30

        +

        combined["Demand 30D"] * 0.20
    )

    # ========================================================
    # FALLBACK
    # ========================================================

    combined["Recent Daily Demand"] = np.where(

        weighted_demand > 0,

        weighted_demand,

        combined["Historical Daily Demand"]
    )

    # ========================================================
    # DEMAND TREND (7D vs 30D)
    # ========================================================

    combined["Demand Trend"] = np.where(

        combined["Demand 30D"] > 0,

        combined["Demand 7D"]
        /
        combined["Demand 30D"],

        1.0
    )

    # Limit extreme trend
    combined["Demand Trend"] = (
        combined["Demand Trend"]
        .replace(
            [np.inf, -np.inf],
            1.0
        )
        .fillna(1.0)
        .clip(
            lower=0.70,
            upper=1.40
        )
    )

    # ========================================================
    # FINAL DAILY DEMAND
    #
    # IMPORTANT:
    # We don't multiply weighted demand by trend again.
    # This prevents over-estimation.
    # ========================================================

    combined["Final Daily Demand"] = (
        combined["Recent Daily Demand"]
        .clip(lower=0)
    )

    # ========================================================
    # SMART FORECAST
    # ========================================================

    combined["Forecast Demand"] = (

        combined["Final Daily Demand"]

        *

        future_days
    )

    combined["Forecast Demand"] = (
        combined["Forecast Demand"]
        .clip(lower=0)
    )

    # ========================================================
    # SAFETY STOCK
    # ========================================================

    combined["Safety Stock"] = (

        combined["Forecast Demand"]

        *

        safety_stock_percent

        /

        100
    )

    combined["Safety Stock"] = (
        combined["Safety Stock"]
        .clip(lower=0)
    )

    # ========================================================
    # REQUIRED STOCK
    # ========================================================

    combined["Required Stock"] = (

        combined["Forecast Demand"]

        +

        combined["Safety Stock"]
    )

    combined["Required Stock"] = (
        combined["Required Stock"]
        .clip(lower=0)
    )

    # ========================================================
    # PURCHASE REQUIREMENT
    # ========================================================

    combined["Recommended Purchase"] = np.maximum(

        combined["Required Stock"]

        -

        combined["Current Inventory"],

        0
    )

    combined["Recommended Purchase"] = np.ceil(
        combined["Recommended Purchase"]
    )

    # ========================================================
    # INVENTORY COVER DAYS
    # ========================================================

    combined["Inventory Cover Days"] = np.where(

        combined["Final Daily Demand"] > 0,

        combined["Current Inventory"]
        /
        combined["Final Daily Demand"],

        999
    )

    combined["Inventory Cover Days"] = (
        combined["Inventory Cover Days"]
        .replace(
            [np.inf, -np.inf],
            999
        )
        .fillna(999)
        .clip(lower=0)
    )

    # ========================================================
    # STOCK STATUS
    # ========================================================

    def get_status(row):

        inventory_value = row["Current Inventory"]

        cover = row["Inventory Cover Days"]

        purchase = row["Recommended Purchase"]

        demand = row["Final Daily Demand"]

        # Completely out
        if inventory_value <= 0:
            return "Out of Stock"

        # No sales / no demand
        if demand <= 0:
            return "Excess Stock"

        # Less than 7 days
        if cover < 7:
            return "Critical"

        # Forecast requirement is higher
        if purchase > 0:
            return "Purchase Required"

        # More than twice the forecast period
        if cover > future_days * 2:
            return "Excess Stock"

        return "Healthy"

    combined["Stock Status"] = combined.apply(
        get_status,
        axis=1
    )

    # ========================================================
    # DEMAND CONDITION
    # ========================================================

    def get_demand_condition(row):

        trend = row["Demand Trend"]

        if trend >= 1.15:
            return "Increasing Demand"

        if trend <= 0.85:
            return "Decreasing Demand"

        return "Stable Demand"

    combined["Demand Condition"] = combined.apply(
        get_demand_condition,
        axis=1
    )

    # ========================================================
    # STOCK LEVEL CATEGORY
    # ========================================================

    def get_inventory_level(row):

        stock = row["Current Inventory"]

        cover = row["Inventory Cover Days"]

        if stock <= 0:
            return "Out of Stock"

        if cover < 3:
            return "Very Low"

        if cover < 7:
            return "Low"

        if cover < future_days:
            return "Normal"

        if cover > future_days * 2:
            return "High"

        return "Normal"

    combined["Inventory Level"] = combined.apply(
        get_inventory_level,
        axis=1
    )

    # ========================================================
    # ROUND
    # ========================================================

    calculated_columns = [
        "Historical Daily Demand",
        "Demand 7D",
        "Demand 15D",
        "Demand 30D",
        "Recent Daily Demand",
        "Demand Trend",
        "Final Daily Demand",
        "Forecast Demand",
        "Safety Stock",
        "Required Stock",
        "Recommended Purchase",
        "Inventory Cover Days"
    ]

    for col in calculated_columns:

        combined[col] = (
            combined[col]
            .round(2)
        )

    return (
        combined,
        inventory,
        sales,
        inventory_raw,
        sales_raw,
        inventory_detected,
        sales_detected,
        history_days,
        latest_snapshot,
    )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        font-size:28px;
        font-weight:800;
        color:white;
        margin-bottom:5px;
    ">
        PROKART
    </div>

    <div style="
        font-size:12px;
        color:#cbd5e1;
        margin-bottom:25px;
    ">
        INVENTORY INTELLIGENCE
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 📁 Data Upload")

inventory_file = st.sidebar.file_uploader(
    "📦 Inventory File",
    type=["xlsx", "xls", "csv"],
    key="inventory_upload"
)

sales_file = st.sidebar.file_uploader(
    "🛒 Sales File",
    type=["xlsx", "xls", "csv"],
    key="sales_upload"
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
<style>

[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: white !important;
}

[data-testid="stSidebar"] div[data-baseweb="select"] * {
    color: black !important;
    font-weight: 400 !important;
}

</style>
""", unsafe_allow_html=True)

future_days = st.sidebar.selectbox(
    "Forecast Period",
    [30, 45],
    index=1
)

safety_stock_percent = st.sidebar.slider(
    "Safety Stock",
    0,
    50,
    10,
    5
)


# ============================================================
# HEADER
# ============================================================

# ============================================================
# WAIT FOR FILES
# ============================================================

if not inventory_file or not sales_file:

    # ========================================================
    # FULL-WIDTH TOP IMAGE
    # ========================================================

    image_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "main.png"
    )

    if os.path.exists(image_path):

        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        image_base64 = base64.b64encode(
            image_bytes
        ).decode("utf-8")

        st.markdown(
            f"""
            <style>

            .prokart-topic-image {{
                width: 100vw !important;
                height: 600px !important;

                margin-left: calc(50% - 50vw) !important;
                margin-right: calc(50% - 50vw) !important;

                margin-top: 10px !important;
                margin-bottom: 30px !important;

                background-image:
                    url("data:image/png;base64,{image_base64}");

                background-size: cover !important;
                background-position: center center !important;
                background-repeat: no-repeat !important;

                border-radius: 0 !important;

                overflow: hidden !important;
            }}

            .prokart-topic-image::after {{
                content: "";
                position: absolute;
                inset: 0;

                background:
                    linear-gradient(
                        90deg,
                        rgba(5,24,45,0.10),
                        rgba(5,24,45,0.02)
                    );

                pointer-events: none;
            }}

            @media (max-width: 900px) {{
                .prokart-topic-image {{
                    width: 7vw !important;
                    height: 450px !important;

                    margin-left: calc(50% - 50vw) !important;
                    margin-right: calc(50% - 50vw) !important;
                }}
            }}

            </style>

            <div class="prokart-topic-image"></div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning("Image file not found: main.png")


    # ========================================================
    # TEXT AFTER IMAGE
    # ========================================================

    st.info(
        "Upload both the Inventory File and Sales File "
        "from the sidebar to start the analysis."
    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            """
            ### 📦 Inventory File

            Know your stock before it runs out.

            Upload your inventory data and instantly explore
            available stock, warehouse levels, low-stock items,
            and products that need replenishment.

            **→ Upload • Analyze • Take Action**
            """
        )


    with col2:

        st.markdown(
            """
            ### 🛒 Sales File

            Turn your sales history into smarter decisions.

            Upload your sales data to discover top-selling products,
            demand patterns, revenue trends, and future stock
            requirements.

            **→ Upload • Discover • Forecast**
            """
        )


    # ========================================================
    # STOP HERE
    # ========================================================

    st.stop()

# ============================================================
# AFTER BOTH FILES ARE UPLOADED
# ============================================================
# Your normal processing/dashboard code starts below this line.


# ============================================================
# PROCESS FILES
# ============================================================

try:

    (
        combined,
        inventory,
        sales,
        inventory_raw,
        sales_raw,
        inventory_detected,
        sales_detected,
        history_days,
        latest_snapshot,
    ) = process_data(
        inventory_file,
        sales_file,
        future_days,
        safety_stock_percent,
    )

    st.success(
        "✓ Inventory and Sales files loaded successfully"
    )

    # ========================================================
    # DASHBOARD KPIs
    # ========================================================

    total_products = len(combined)

    total_sales = combined[
        "Quantity"
    ].sum()

    total_inventory = combined[
        "Current Inventory"
    ].sum()

    total_revenue = combined[
        "Gross Amount"
    ].sum()

    total_forecast = combined[
        "Forecast Demand"
    ].sum()

    total_purchase = combined[
        "Recommended Purchase"
    ].sum()

    out_stock = (
        combined["Stock Status"]
        ==
        "Out of Stock"
    ).sum()

    critical_stock = (
        combined["Stock Status"]
        ==
        "Critical"
    ).sum()


    # ========================================================
    # BUSINESS OVERVIEW
    # ========================================================

    st.markdown(
        '<div class="section-title">Business Overview</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        kpi_card(
            "📦",
            "Total Products",
            f"{total_products:,}"
        )


    with c2:

        kpi_card(
            "🛒",
            "Units Sold",
            f"{total_sales:,.0f}"
        )


    with c3:

        kpi_card(
            "💰",
            "Sales Revenue",
            f"₹{total_revenue:,.0f}"
        )


    with c4:

        kpi_card(
            "🏬",
            "Current Stock",
            f"{total_inventory:,.0f}"
        )


    st.write("")


    c5, c6, c7, c8 = st.columns(4)


    with c5:

        kpi_card(
            "📈",
            f"{future_days}-Day Forecast",
            f"{total_forecast:,.0f}"
        )


    with c6:

        kpi_card(
            "🛍️",
            "Purchase Required",
            f"{total_purchase:,.0f}"
        )


    with c7:

        kpi_card(
            "⚠️",
            "Critical Products",
            f"{critical_stock:,}"
        )


    with c8:

        kpi_card(
            "🚫",
            "Out of Stock",
            f"{out_stock:,}"
        )


    # ========================================================
    # FILTERS
    # ========================================================

    st.markdown(
        '<div class="section-title">🔎 Inventory Filters</div>',
        unsafe_allow_html=True
    )


    f1, f2, f3 = st.columns(3)


    with f1:

        search_text = st.text_input(
            "Search Product / Item ID",
            placeholder="Type product or Item ID..."
        )


    with f2:

        status_filter = st.selectbox(
            "Stock Status",
            [
                "All",
                "Healthy",
                "Purchase Required",
                "Critical",
                "Out of Stock",
                "Excess Stock"
            ]
        )


    with f3:

        brand_list = sorted(
            combined["Brand"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_brand = st.selectbox(
            "Brand",
            ["All"] + brand_list
        )


    filtered = combined.copy()


    if search_text:

        search_lower = search_text.lower()

        filtered = filtered[
            filtered["Item ID"]
            .astype(str)
            .str.lower()
            .str.contains(
                search_lower,
                na=False
            )
            |
            filtered["Product Name"]
            .astype(str)
            .str.lower()
            .str.contains(
                search_lower,
                na=False
            )
        ]


    if status_filter != "All":

        filtered = filtered[
            filtered["Stock Status"]
            ==
            status_filter
        ]


    if selected_brand != "All":

        filtered = filtered[
            filtered["Brand"]
            ==
            selected_brand
        ]
                                             

    # ========================================================
    # SALES TREND
    # ========================================================

    st.markdown(
        '<div class="section-title">📈 Sales Trend</div>',
        unsafe_allow_html=True
    )

 
    if sales["Order Date"].notna().any():

        daily_sales = (
            sales
            .dropna(
                subset=["Order Date"]
            )
            .assign(
                Sales_Day=lambda x:
                x["Order Date"].dt.floor("D")
            )
            .groupby(
                "Sales_Day"
            )["Quantity"]
            .sum()
            .reset_index()
        )

        daily_sales = daily_sales.sort_values(
            "Sales_Day"
        )

        st.line_chart(
            daily_sales.set_index(
                "Sales_Day"
            )["Quantity"],
            height=300
        )

    else:

        st.info(
            "Order Date was not detected, so the sales trend cannot be displayed."
        )


    # ========================================================
    # CHART SECTION
    # ========================================================
























    chart1, chart2 = st.columns(2)


    # ========================================================
    # STOCK STATUS
    # ========================================================

    with chart1:

        st.markdown(
            '<div class="section-title">📊 Stock Health</div>',
            unsafe_allow_html=True
        )


        status_chart = (
            combined["Stock Status"]
            .value_counts()
            .rename_axis("Status")
            .reset_index(
                name="Products"
            )
        )


        st.bar_chart(
            status_chart.set_index(
                "Status"
            )["Products"],
            height=300
        )


    # ========================================================
    # TOP PRODUCTS
    # ========================================================

    with chart2:

        st.markdown(
            '<div class="section-title">🔥 Top Selling Products</div>',
            unsafe_allow_html=True
        )


        top_products = (
            combined
            .sort_values(
                "Quantity",
                ascending=False
            )
            .head(10)
            [
                [
                    "Product Name",
                    "Quantity"
                ]
            ]
        )


        if len(top_products) > 0:

            st.bar_chart(
                top_products.set_index(
                    "Product Name"
                )["Quantity"],
                height=300
            )


    # ========================================================
    # MAIN INVENTORY TABLE
    # ========================================================

    st.markdown(
        '<div class="section-title">📋 Inventory Intelligence</div>',
        unsafe_allow_html=True
    )


    table_columns = [

        "Item ID",

        "Product Name",

        "Brand",

        "Quantity",

        "Current Inventory",

        "Demand 7D",

        "Demand 15D",

        "Demand 30D",

        "Final Daily Demand",

        "Forecast Demand",

        "Safety Stock",

        "Required Stock",

        "Inventory Cover Days",

        "Recommended Purchase",

        "Demand Condition",

        "Inventory Level",

        "Stock Status"
    ]


    table_columns = [
        c
        for c in table_columns
        if c in filtered.columns
    ]


    st.dataframe(
        filtered[
            table_columns
        ],
        use_container_width=True,
        height=500,
        hide_index=True
    )


    # ========================================================
    # LOW INVENTORY ANALYSIS
    # ========================================================

    st.markdown(
        '<div class="section-title">🔻 Low Inventory Analysis</div>',
        unsafe_allow_html=True
    )


    low_inventory = combined[
        (
            combined["Inventory Level"].isin(
                [
                    "Very Low",
                    "Low",
                    "Out of Stock"
                ]
            )
        )
    ].copy()


    low_inventory = low_inventory.sort_values(
        [
            "Inventory Cover Days",
            "Recommended Purchase"
        ],
        ascending=[
            True,
            False
        ]
    )


    if len(low_inventory) == 0:

        st.success(
            "✓ No low inventory products detected."
        )

    else:

        low_columns = [

            "Item ID",

            "Product Name",

            "Brand",

            "Current Inventory",

            "Final Daily Demand",

            "Inventory Cover Days",

            "Forecast Demand",

            "Required Stock",

            "Recommended Purchase",

            "Inventory Level",

            "Stock Status"
        ]

        st.dataframe(
            low_inventory[
                low_columns
            ],
            use_container_width=True,
            height=400,
            hide_index=True
        )


    # ========================================================
    # PURCHASE RECOMMENDATIONS
    # ========================================================

    st.markdown(
        '<div class="section-title">🛍️ Purchase Recommendations</div>',
        unsafe_allow_html=True
    )


    purchase_data = combined[
        combined["Recommended Purchase"] > 0
    ].copy()


    purchase_data = purchase_data.sort_values(
        "Recommended Purchase",
        ascending=False
    )


    if len(purchase_data) == 0:

        st.success(
            "✓ No additional purchase is currently required."
        )

    else:

        purchase_columns = [

            "Item ID",

            "Product Name",

            "Current Inventory",

            "Demand Condition",

            "Forecast Demand",

            "Safety Stock",

            "Required Stock",

            "Recommended Purchase",

            "Inventory Cover Days",

            "Stock Status"
        ]


        st.dataframe(
            purchase_data[
                purchase_columns
            ],
            use_container_width=True,
            height=400,
            hide_index=True
        )


    # ========================================================
    # CRITICAL ALERTS
    # ========================================================

    st.markdown(
        '<div class="section-title">🚨 Inventory Alerts</div>',
        unsafe_allow_html=True
    )


    critical_products = combined[
        combined["Stock Status"].isin(
            [
                "Out of Stock",
                "Critical"
            ]
        )
    ].copy()


    critical_products = critical_products.sort_values(
        "Inventory Cover Days",
        ascending=True
    )


    if len(critical_products) == 0:

        st.success(
            "✓ No critical inventory alerts."
        )

    else:

        for _, row in critical_products.head(10).iterrows():

            st.markdown(
                f"""
                <div class="alert-card danger-card">
                    <b>{row["Product Name"]}</b>
                    &nbsp; | &nbsp;
                    Item ID: {row["Item ID"]}
                    &nbsp; | &nbsp;
                    Current Stock: {row["Current Inventory"]:,.0f}
                    &nbsp; | &nbsp;
                    Daily Demand: {row["Final Daily Demand"]:,.2f}
                    &nbsp; | &nbsp;
                    Cover: {row["Inventory Cover Days"]:,.1f} days
                    &nbsp; | &nbsp;
                    <b>{row["Stock Status"]}</b>
                </div>
                """,
                unsafe_allow_html=True
            )


    # ========================================================
    # STATE ANALYSIS
    # ========================================================

    st.markdown(
        '<div class="section-title">🌎 State-wise Sales</div>',
        unsafe_allow_html=True
    )


    def order_count(group):

        if (
            "Order ID" in group.columns
            and
            group["Order ID"].notna().any()
        ):

            return group["Order ID"].nunique()

        return len(group)


    state_rows = []

    for state, group in sales.groupby(
        "State",
        dropna=False
    ):

        state_rows.append({

            "State": (
                "Unknown"
                if pd.isna(state)
                else str(state)
            ),

            "Units Sold":
                group["Quantity"].sum(),

            "Revenue":
                group["Gross Amount"].sum(),

            "Orders":
                order_count(group),

            "Products":
                group["Item ID"].nunique(),

            "Cities":
                group["City"].nunique()
        })


    state_sales = pd.DataFrame(
        state_rows
    )


    if len(state_sales) > 0:

        state_sales = state_sales.sort_values(
            "Units Sold",
            ascending=False
        )

        state_col1, state_col2 = st.columns(2)


        with state_col1:

            st.dataframe(
                state_sales,
                use_container_width=True,
                hide_index=True
            )


        with state_col2:

            st.bar_chart(
                state_sales.set_index(
                    "State"
                )["Units Sold"],
                height=350
            )


    # ========================================================
    # CITY-WISE SALES
    # ========================================================

    st.markdown(
        '<div class="section-title">🏙️ City-wise Sales</div>',
        unsafe_allow_html=True
    )


    city_rows = []

    for (
        state,
        city
    ), group in sales.groupby(
        [
            "State",
            "City"
        ],
        dropna=False
    ):

        state_name = (
            "Unknown"
            if pd.isna(state)
            else str(state)
        )

        city_name = (
            "Unknown"
            if pd.isna(city)
            else str(city)
        )

        city_rows.append({

            "State":
                state_name,

            "City":
                city_name,

            "Units Sold":
                group["Quantity"].sum(),

            "Revenue":
                group["Gross Amount"].sum(),

            "Orders":
                order_count(group),

            "Products":
                group["Item ID"].nunique(),

            "Avg Units / Order":
                (
                    group["Quantity"].sum()
                    /
                    max(order_count(group), 1)
                )
        })


    city_sales = pd.DataFrame(
        city_rows
    )


    if len(city_sales) > 0:

        city_sales = city_sales.sort_values(
            "Units Sold",
            ascending=False
        )

        city_col1, city_col2 = st.columns(2)


        with city_col1:

            st.dataframe(
                city_sales,
                use_container_width=True,
                height=400,
                hide_index=True
            )


        with city_col2:

            top_cities = (
                city_sales
                .head(15)
                .copy()
            )

            if len(top_cities) > 0:

                city_chart = (
                    top_cities
                    .assign(
                        City_Display=lambda x:
                        x["City"]
                        + " ("
                        + x["State"]
                        + ")"
                    )
                )

                st.bar_chart(
                    city_chart.set_index(
                        "City_Display"
                    )["Units Sold"],
                    height=400
                )

    else:

        st.info(
            "City information was not found in the Sales file."
        )


    # ========================================================
    # CITY + PRODUCT ANALYSIS
    # ========================================================

    st.markdown(
        '<div class="section-title">📍 City Product Performance</div>',
        unsafe_allow_html=True
    )


    city_product = (
        sales
        .groupby(
            [
                "State",
                "City",
                "Item ID",
                "Product Name"
            ],
            as_index=False
        )
        .agg(
            Units_Sold=(
                "Quantity",
                "sum"
            ),
            Revenue=(
                "Gross Amount",
                "sum"
            )
        )
        .sort_values(
            "Units_Sold",
            ascending=False
        )
        .head(100)
    )


    if len(city_product) > 0:

        st.dataframe(
            city_product,
            use_container_width=True,
            height=350,
            hide_index=True
        )


    # ========================================================
    # PRODUCT DETAIL
    # ========================================================

    st.markdown(
        '<div class="section-title">🔍 Product Detail</div>',
        unsafe_allow_html=True
    )


    product_ids = sorted(
        sales["Item ID"]
        .astype(str)
        .unique()
        .tolist()
    )


    selected_item = st.selectbox(
        "Select Item ID",
        ["Select Product"] + product_ids
    )


    if selected_item != "Select Product":

        product_sales = sales[
            sales["Item ID"].astype(str)
            ==
            str(selected_item)
        ].copy()


        if len(product_sales) > 0:

            p1, p2, p3, p4 = st.columns(4)


            product_total = (
                product_sales["Quantity"]
                .sum()
            )


            product_revenue = (
                product_sales["Gross Amount"]
                .sum()
            )


            product_orders = order_count(
                product_sales
            )


            product_states = (
                product_sales["State"]
                .nunique()
            )


            with p1:

                kpi_card(
                    "🛒",
                    "Units Sold",
                    f"{product_total:,.0f}"
                )


            with p2:

                kpi_card(
                    "💰",
                    "Revenue",
                    f"₹{product_revenue:,.0f}"
                )


            with p3:

                kpi_card(
                    "🧾",
                    "Orders",
                    f"{product_orders:,}"
                )


            with p4:

                kpi_card(
                    "🌎",
                    "States",
                    f"{product_states:,}"
                )


            # Product inventory information

            selected_inventory = combined[
                combined["Item ID"].astype(str)
                ==
                str(selected_item)
            ]


            if len(selected_inventory) > 0:

                inv_row = selected_inventory.iloc[0]

                st.info(
                    f"""
                    📦 Current Stock: **{inv_row["Current Inventory"]:,.0f}**
                    &nbsp;&nbsp; | &nbsp;&nbsp;
                    📈 Daily Demand: **{inv_row["Final Daily Demand"]:,.2f}**
                    &nbsp;&nbsp; | &nbsp;&nbsp;
                    ⏳ Stock Cover: **{inv_row["Inventory Cover Days"]:,.1f} days**
                    &nbsp;&nbsp; | &nbsp;&nbsp;
                    🛍️ Purchase: **{inv_row["Recommended Purchase"]:,.0f}**
                    """
                )


            st.dataframe(
                product_sales,
                use_container_width=True,
                height=300,
                hide_index=True
            )


    # ========================================================
    # DATA INFORMATION
    # ========================================================

    with st.expander("📁 Data Information"):

        info1, info2 = st.columns(2)


        with info1:

            st.write("### Inventory File")

            st.write(
                f"Rows: **{len(inventory_raw):,}**"
            )

            st.write(
                f"Columns: **{len(inventory_raw.columns):,}**"
            )

            st.write(
                "Detected Item ID: "
                f"**{inventory_detected['item_id']}**"
            )

            st.write(
                "Detected Inventory: "
                f"**{inventory_detected['inventory']}**"
            )

            st.write(
                "Detected Snapshot: "
                f"**{inventory_detected['snapshot']}**"
            )


        with info2:

            st.write("### Sales File")

            st.write(
                f"Rows: **{len(sales_raw):,}**"
            )

            st.write(
                f"Columns: **{len(sales_raw.columns):,}**"
            )

            st.write(
                "Detected Item ID: "
                f"**{sales_detected['item_id']}**"
            )

            st.write(
                "Detected Quantity: "
                f"**{sales_detected['quantity']}**"
            )

            st.write(
                "Detected State: "
                f"**{sales_detected['state']}**"
            )

            st.write(
                "Detected City: "
                f"**{sales_detected['city']}**"
            )

            st.write(
                "Detected Pincode: "
                f"**{sales_detected['pincode']}**"
            )


        st.write(
            f"Historical sales period: "
            f"**{history_days} days**"
        )


        if latest_snapshot is not None:

            st.write(
                "Latest inventory snapshot: "
                f"**{latest_snapshot.strftime('%Y-%m-%d')}**"
            )


    # ========================================================
    # EXCEL REPORT
    # ========================================================

    st.markdown(
        '<div class="section-title">📥 Reports</div>',
        unsafe_allow_html=True
    )


    excel_output = io.BytesIO()


    with pd.ExcelWriter(
        excel_output,
        engine="openpyxl"
    ) as writer:

        combined.to_excel(
            writer,
            sheet_name="Inventory Analysis",
            index=False
        )

        sales.to_excel(
            writer,
            sheet_name="Sales Data",
            index=False
        )

        inventory.to_excel(
            writer,
            sheet_name="Inventory Data",
            index=False
        )

        purchase_data.to_excel(
            writer,
            sheet_name="Purchase Recommendations",
            index=False
        )

        low_inventory.to_excel(
            writer,
            sheet_name="Low Inventory",
            index=False
        )

        critical_products.to_excel(
            writer,
            sheet_name="Critical Alerts",
            index=False
        )

        state_sales.to_excel(
            writer,
            sheet_name="State Sales",
            index=False
        )

        city_sales.to_excel(
            writer,
            sheet_name="City Sales",
            index=False
        )

        city_product.to_excel(
            writer,
            sheet_name="City Product Sales",
            index=False
        )


    excel_output.seek(0)


    st.download_button(
        label="📥 Download ProKart Inventory Report",
        data=excel_output,
        file_name="ProKart_Inventory_Intelligence_Report.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )


    # ========================================================
    # FOOTER
    # ========================================================

    st.markdown(
        """
        <br><br>
        <div style="
            text-align:center;
            color:#98A2B3;
            font-size:12px;
            padding:20px;
        ">
            ProKart Inventory Intelligence
            &nbsp; • &nbsp;
            Sales & Inventory Analytics
        </div>
        """,
        unsafe_allow_html=True
    )


except Exception as e:

    st.error(
        f"❌ Unable to process the uploaded files: {e}"
    )

    st.warning(
        "Please check that the Inventory file contains "
        "Item ID/SKU/ASIN and the Sales file contains "
        "Item ID/SKU/ASIN. Quantity is optional for order-level sales data."
    )

    with st.expander("🛠️ Technical details (for debugging)"):

        st.code(traceback.format_exc())