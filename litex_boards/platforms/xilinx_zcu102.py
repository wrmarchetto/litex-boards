#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2022 FAYE Joseph <joseph-wagane.faye@insa-rennes.fr>
# Copyright (c) 2023 Ryohei Niwase <niwase@lila.cs.tsukuba.ac.jp>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxUSPPlatform, VivadoProgrammer


# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk125", 0,
        Subsignal("p", Pins("G21"), IOStandard("LVDS_25")),
        Subsignal("n", Pins("F21"), IOStandard("LVDS_25")),
    ),
    ("clk300", 0,
        Subsignal("p", Pins("AL8"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("n", Pins("AL7"), IOStandard("DIFF_SSTL12_DCI")),
    ),
    ("cpu_reset", 0, Pins("AM13"), IOStandard("LVCMOS33")),

    # Leds
    ("user_led", 0, Pins("AG14"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("AF13"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("AE13"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("AJ14"), IOStandard("LVCMOS33")),
    ("user_led", 4, Pins("AJ15"), IOStandard("LVCMOS33")),
    ("user_led", 5, Pins("AH13"), IOStandard("LVCMOS33")),
    ("user_led", 6, Pins("AH14"), IOStandard("LVCMOS33")),
    ("user_led", 7, Pins("AL12"), IOStandard("LVCMOS33")),

    # Buttons
    ("user_btn", 0, Pins("AG15"), IOStandard("LVCMOS33")),
    ("user_btn", 1, Pins("AE14"), IOStandard("LVCMOS33")),
    ("user_btn", 2, Pins("AF15"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("AE15"), IOStandard("LVCMOS33")),
    ("user_btn", 3, Pins("AG13"), IOStandard("LVCMOS33")),

    # Switches
    ("user_dip", 0, Pins("AN14"), IOStandard("LVCMOS33")),
    ("user_dip", 1, Pins("AP14"), IOStandard("LVCMOS33")),
    ("user_dip", 2, Pins("AM14"), IOStandard("LVCMOS33")),
    ("user_dip", 3, Pins("AN13"), IOStandard("LVCMOS33")),
    ("user_dip", 4, Pins("AN12"), IOStandard("LVCMOS33")),
    ("user_dip", 5, Pins("AP12"), IOStandard("LVCMOS33")),
    ("user_dip", 6, Pins("AL13"), IOStandard("LVCMOS33")),
    ("user_dip", 7, Pins("AK13"), IOStandard("LVCMOS33")),

    # Serial
    ("serial", 0,
        Subsignal("cts", Pins("E12")),
        Subsignal("rts", Pins("D12")),
        Subsignal("rx",  Pins("E13")),
        Subsignal("tx",  Pins("F13")),
        IOStandard("LVCMOS33")
    ),

    # I2C
    ("i2c", 0,
        Subsignal("sda", Pins("J11")),
        Subsignal("scl", Pins("J10")),
        IOStandard("LVCMOS33")
    ),

    # DDR4 SDRAM
    ("ddram", 0,
        Subsignal("a",       Pins(
            "AM8  AM9  AP8  AN8  AK10 AJ10 AP9  AN9",
            "AP10 AP11 AM10 AL10 AM11 AL11"),
            IOStandard("SSTL12_DCI")),
        Subsignal("ba",      Pins("AK12 AJ12"), IOStandard("SSTL12_DCI")),
        Subsignal("bg",      Pins("AK7"), IOStandard("SSTL12_DCI")),
        Subsignal("ras_n",   Pins("AJ9"), IOStandard("SSTL12_DCI")), # A16
        Subsignal("cas_n",   Pins("AL5"), IOStandard("SSTL12_DCI")), # A15
        Subsignal("we_n",    Pins("AJ7"), IOStandard("SSTL12_DCI")), # A14
        Subsignal("cs_n",    Pins("AP2"), IOStandard("SSTL12_DCI")),
        Subsignal("act_n",   Pins("AK8"), IOStandard("SSTL12_DCI")),
        #Subsignal("par",     Pins("AP1"), IOStandard("SSTL12_DCI")),
        Subsignal("dm",      Pins("AL6 AN2"),
            IOStandard("POD12_DCI")),
        Subsignal("dq",      Pins(
                "AK4 AK5 AN4 AM4 AP4 AP5 AM5 AM6",
                "AK2 AK3 AL1 AK1 AN1 AM1 AP3 AN3"),
            IOStandard("POD12_DCI"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_p",   Pins("AN6 AL3"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_n",   Pins("AP6 AL2"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("clk_p",   Pins("AN7"), IOStandard("DIFF_SSTL12")),
        Subsignal("clk_n",   Pins("AP7"), IOStandard("DIFF_SSTL12")),
        Subsignal("cke",     Pins("AM3"), IOStandard("SSTL12_DCI")),
        Subsignal("odt",     Pins("AK9"), IOStandard("SSTL12_DCI")),
        Subsignal("reset_n", Pins("AH9"), IOStandard("LVCMOS18")),
        Misc("SLEW=FAST"),
    ),

    # GTP RefClk common to all SFPs.
    ("mgt_refclk", 0,
        Subsignal("p", Pins("C8")),
        Subsignal("n", Pins("C7")),
    ),

    # SFP.
    # Right Top (GT Location: X1Y12).
    ("sfp_tx_disable_n", 0, Pins("A12"), IOStandard("LVCMOS33")),
    ("sfp", 0,
        Subsignal("txp", Pins("E4")),
        Subsignal("txn", Pins("E3")),
        Subsignal("rxp", Pins("D2")),
        Subsignal("rxn", Pins("D1")),
    ),
    ("sfp_tx", 0,
        Subsignal("p", Pins("E4")),
        Subsignal("n", Pins("E3")),
    ),
    ("sfp_rx", 0,
        Subsignal("p", Pins("D2")),
        Subsignal("n", Pins("D1")),
    ),

    # Right Bottom (GT Location: X1Y13).
    ("sfp_tx_disable_n", 1, Pins("A13"), IOStandard("LVCMOS33")),
    ("sfp", 1,
        Subsignal("txp", Pins("D6")),
        Subsignal("txn", Pins("D5")),
        Subsignal("rxp", Pins("C4")),
        Subsignal("rxn", Pins("C3")),
    ),
    ("sfp_tx", 1,
        Subsignal("p", Pins("D6")),
        Subsignal("n", Pins("D5")),
    ),
    ("sfp_rx", 1,
        Subsignal("p", Pins("C4")),
        Subsignal("n", Pins("C3")),
    ),

    # Left Top (GT Location: X1Y14).
    ("sfp_tx_disable_n", 2, Pins("B13"), IOStandard("LVCMOS33")),
    ("sfp", 2,
        Subsignal("txp", Pins("B6")),
        Subsignal("txn", Pins("B5")),
        Subsignal("rxp", Pins("B2")),
        Subsignal("rxn", Pins("B1")),
    ),
    ("sfp_tx", 2,
        Subsignal("p", Pins("B6")),
        Subsignal("n", Pins("B5")),
    ),
    ("sfp_rx", 2,
        Subsignal("p", Pins("B2")),
        Subsignal("n", Pins("B1")),
    ),

    # Left Bottom (GT Location: X1Y15).
    ("sfp_tx_disable_n", 3, Pins("C13"), IOStandard("LVCMOS33")),
    ("sfp", 3,
        Subsignal("txp", Pins("A8")),
        Subsignal("txn", Pins("A7")),
        Subsignal("rxp", Pins("A4")),
        Subsignal("rxn", Pins("A3")),
    ),
    ("sfp_tx", 3,
        Subsignal("p", Pins("A8")),
        Subsignal("n", Pins("A7")),
    ),
    ("sfp_rx", 3,
        Subsignal("p", Pins("A4")),
        Subsignal("n", Pins("A3")),
    ),
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    ("PMOD0", "A20 B20 A22 A21 B21 C21 C22 D21"),
    ("PMOD1", "D20 E20 D22 E22 F20 G20 J20 J19"),
    ("FMC_HPC0", {                  # FMC connector pin
        "DP1_M2C_P"       : "J4",   # A2  (MGT, not usable as GPIO)
        "DP1_M2C_N"       : "J3",   # A3  (MGT, not usable as GPIO)
        "DP2_M2C_P"       : "F2",   # A6  (MGT, not usable as GPIO)
        "DP2_M2C_N"       : "F1",   # A7  (MGT, not usable as GPIO)
        "DP3_M2C_P"       : "K2",   # A10 (MGT, not usable as GPIO)
        "DP3_M2C_N"       : "K1",   # A11 (MGT, not usable as GPIO)
        "DP4_M2C_P"       : "L4",   # A14 (MGT, not usable as GPIO)
        "DP4_M2C_N"       : "L3",   # A15 (MGT, not usable as GPIO)
        "DP5_M2C_P"       : "P2",   # A18 (MGT, not usable as GPIO)
        "DP5_M2C_N"       : "P1",   # A19 (MGT, not usable as GPIO)
        "DP1_C2M_P"       : "H6",   # A22 (MGT, not usable as GPIO)
        "DP1_C2M_N"       : "H5",   # A23 (MGT, not usable as GPIO)
        "DP2_C2M_P"       : "F6",   # A26 (MGT, not usable as GPIO)
        "DP2_C2M_N"       : "F5",   # A27 (MGT, not usable as GPIO)
        "DP3_C2M_P"       : "K6",   # A30 (MGT, not usable as GPIO)
        "DP3_C2M_N"       : "K5",   # A31 (MGT, not usable as GPIO)
        "DP4_C2M_P"       : "M6",   # A34 (MGT, not usable as GPIO)
        "DP4_C2M_N"       : "M5",   # A35 (MGT, not usable as GPIO)
        "DP5_C2M_P"       : "P6",   # A38 (MGT, not usable as GPIO)
        "DP5_C2M_N"       : "P5",   # A39 (MGT, not usable as GPIO)
        "DP7_M2C_P"       : "M2",   # B12 (MGT, not usable as GPIO)
        "DP7_M2C_N"       : "M1",   # B13 (MGT, not usable as GPIO)
        "DP6_M2C_P"       : "T2",   # B16 (MGT, not usable as GPIO)
        "DP6_M2C_N"       : "T1",   # B17 (MGT, not usable as GPIO)
        "GBTCLK1_M2C_P"   : "L8",   # B20 (reference clock, not usable as GPIO)
        "GBTCLK1_M2C_N"   : "L7",   # B21 (reference clock, not usable as GPIO)
        "DP7_C2M_P"       : "N4",   # B32 (MGT, not usable as GPIO)
        "DP7_C2M_N"       : "N3",   # B33 (MGT, not usable as GPIO)
        "DP6_C2M_P"       : "R4",   # B36 (MGT, not usable as GPIO)
        "DP6_C2M_N"       : "R3",   # B37 (MGT, not usable as GPIO)
        "DP0_C2M_P"       : "G4",   # C2  (MGT, not usable as GPIO)
        "DP0_C2M_N"       : "G3",   # C3  (MGT, not usable as GPIO)
        "DP0_M2C_P"       : "H2",   # C6  (MGT, not usable as GPIO)
        "DP0_M2C_N"       : "H1",   # C7  (MGT, not usable as GPIO)
        "LA06_P"          : "AC2",  # C10
        "LA06_N"          : "AC1",  # C11
        "LA10_P"          : "W5",   # C14
        "LA10_N"          : "W4",   # C15
        "LA14_P"          : "AC7",  # C18
        "LA14_N"          : "AC6",  # C19
        "LA18_CC_P"       : "N9",   # C22
        "LA18_CC_N"       : "N8",   # C23
        "LA27_P"          : "M10",  # C26
        "LA27_N"          : "L10",  # C27
        "GBTCLK0_M2C_P"   : "G8",   # D4  (reference clock, not usable as GPIO)
        "GBTCLK0_M2C_N"   : "G7",   # D5  (reference clock, not usable as GPIO)
        "LA01_CC_P"       : "AB4",  # D8
        "LA01_CC_N"       : "AC4",  # D9
        "LA05_P"          : "AB3",  # D11
        "LA05_N"          : "AC3",  # D12
        "LA09_P"          : "W2",   # D14
        "LA09_N"          : "W1",   # D15
        "LA13_P"          : "AB8",  # D17
        "LA13_N"          : "AC8",  # D18
        "LA17_CC_P"       : "P11",  # D20
        "LA17_CC_N"       : "N11",  # D21
        "LA23_P"          : "L16",  # D23
        "LA23_N"          : "K16",  # D24
        "LA26_P"          : "L15",  # D26
        "LA26_N"          : "K15",  # D27
        "CLK1_M2C_P"      : "T8",   # G2
        "CLK1_M2C_N"      : "R8",   # G3
        "LA00_CC_P"       : "Y4",   # G6
        "LA00_CC_N"       : "Y3",   # G7
        "LA03_P"          : "Y2",   # G9
        "LA03_N"          : "Y1",   # G10
        "LA08_P"          : "V4",   # G12
        "LA08_N"          : "V3",   # G13
        "LA12_P"          : "W7",   # G15
        "LA12_N"          : "W6",   # G16
        "LA16_P"          : "Y12",  # G18
        "LA16_N"          : "AA12", # G19
        "LA20_P"          : "N13",  # G21
        "LA20_N"          : "M13",  # G22
        "LA22_P"          : "M15",  # G24
        "LA22_N"          : "M14",  # G25
        "LA25_P"          : "M11",  # G27
        "LA25_N"          : "L11",  # G28
        "LA29_P"          : "U9",   # G30
        "LA29_N"          : "U8",   # G31
        "LA31_P"          : "V8",   # G33
        "LA31_N"          : "V7",   # G34
        "LA33_P"          : "V12",  # G36
        "LA33_N"          : "V11",  # G37
        "CLK0_M2C_P"      : "AA7",  # H4
        "CLK0_M2C_N"      : "AA6",  # H5
        "LA02_P"          : "V2",   # H7
        "LA02_N"          : "V1",   # H8
        "LA04_P"          : "AA2",  # H10
        "LA04_N"          : "AA1",  # H11
        "LA07_P"          : "U5",   # H13
        "LA07_N"          : "U4",   # H14
        "LA11_P"          : "AB6",  # H16
        "LA11_N"          : "AB5",  # H17
        "LA15_P"          : "Y10",  # H19
        "LA15_N"          : "Y9",   # H20
        "LA19_P"          : "L13",  # H22
        "LA19_N"          : "K13",  # H23
        "LA21_P"          : "P12",  # H25
        "LA21_N"          : "N12",  # H26
        "LA24_P"          : "L12",  # H28
        "LA24_N"          : "K12",  # H29
        "LA28_P"          : "T7",   # H31
        "LA28_N"          : "T6",   # H32
        "LA30_P"          : "V6",   # H34
        "LA30_N"          : "U6",   # H35
        "LA32_P"          : "U11",  # H37
        "LA32_N"          : "T11",  # H38
    }),
    ("FMC_HPC1", {                  # FMC connector pin
        "DP1_M2C_P"       : "D33",  # A2  (MGT, not usable as GPIO)
        "DP1_M2C_N"       : "D34",  # A3  (MGT, not usable as GPIO)
        "DP2_M2C_P"       : "C31",  # A6  (MGT, not usable as GPIO)
        "DP2_M2C_N"       : "C32",  # A7  (MGT, not usable as GPIO)
        "DP3_M2C_P"       : "B33",  # A10 (MGT, not usable as GPIO)
        "DP3_M2C_N"       : "B34",  # A11 (MGT, not usable as GPIO)
        "DP4_M2C_P"       : "L31",  # A14 (MGT, not usable as GPIO)
        "DP4_M2C_N"       : "L32",  # A15 (MGT, not usable as GPIO)
        "DP5_M2C_P"       : "K33",  # A18 (MGT, not usable as GPIO)
        "DP5_M2C_N"       : "K34",  # A19 (MGT, not usable as GPIO)
        "DP1_C2M_P"       : "D29",  # A22 (MGT, not usable as GPIO)
        "DP1_C2M_N"       : "D30",  # A23 (MGT, not usable as GPIO)
        "DP2_C2M_P"       : "B29",  # A26 (MGT, not usable as GPIO)
        "DP2_C2M_N"       : "B30",  # A27 (MGT, not usable as GPIO)
        "DP3_C2M_P"       : "A31",  # A30 (MGT, not usable as GPIO)
        "DP3_C2M_N"       : "A32",  # A31 (MGT, not usable as GPIO)
        "DP4_C2M_P"       : "K29",  # A34 (MGT, not usable as GPIO)
        "DP4_C2M_N"       : "K30",  # A35 (MGT, not usable as GPIO)
        "DP5_C2M_P"       : "J31",  # A38 (MGT, not usable as GPIO)
        "DP5_C2M_N"       : "J32",  # A39 (MGT, not usable as GPIO)
        "DP7_M2C_P"       : "F33",  # B12 (MGT, not usable as GPIO)
        "DP7_M2C_N"       : "F34",  # B13 (MGT, not usable as GPIO)
        "DP6_M2C_P"       : "H33",  # B16 (MGT, not usable as GPIO)
        "DP6_M2C_N"       : "H34",  # B17 (MGT, not usable as GPIO)
        "GBTCLK1_M2C_P"   : "E27",  # B20 (reference clock, not usable as GPIO)
        "GBTCLK1_M2C_N"   : "E28",  # B21 (reference clock, not usable as GPIO)
        "DP7_C2M_P"       : "G31",  # B32 (MGT, not usable as GPIO)
        "DP7_C2M_N"       : "G32",  # B33 (MGT, not usable as GPIO)
        "DP6_C2M_P"       : "H29",  # B36 (MGT, not usable as GPIO)
        "DP6_C2M_N"       : "H30",  # B37 (MGT, not usable as GPIO)
        "DP0_C2M_P"       : "F29",  # C2  (MGT, not usable as GPIO)
        "DP0_C2M_N"       : "F30",  # C3  (MGT, not usable as GPIO)
        "DP0_M2C_P"       : "E31",  # C6  (MGT, not usable as GPIO)
        "DP0_M2C_N"       : "E32",  # C7  (MGT, not usable as GPIO)
        "LA06_P"          : "AH2",  # C10
        "LA06_N"          : "AJ2",  # C11
        "LA10_P"          : "AH4",  # C14
        "LA10_N"          : "AJ4",  # C15
        "LA14_P"          : "AH7",  # C18
        "LA14_N"          : "AH6",  # C19
        "LA18_CC_P"       : "Y8",   # C22
        "LA18_CC_N"       : "Y7",   # C23
        "LA27_P"          : "U10",  # C26
        "LA27_N"          : "T10",  # C27
        "GBTCLK0_M2C_P"   : "G27",  # D4  (reference clock, not usable as GPIO)
        "GBTCLK0_M2C_N"   : "G28",  # D5  (reference clock, not usable as GPIO)
        "LA01_CC_P"       : "AJ6",  # D8
        "LA01_CC_N"       : "AJ5",  # D9
        "LA05_P"          : "AG3",  # D11
        "LA05_N"          : "AH3",  # D12
        "LA09_P"          : "AE2",  # D14
        "LA09_N"          : "AE1",  # D15
        "LA13_P"          : "AG8",  # D17
        "LA13_N"          : "AH8",  # D18
        "LA17_CC_P"       : "Y5",   # D20
        "LA17_CC_N"       : "AA5",  # D21
        "LA23_P"          : "AE12", # D23
        "LA23_N"          : "AF12", # D24
        "LA26_P"          : "T12",  # D26
        "LA26_N"          : "R12",  # D27
        "CLK1_M2C_P"      : "P10",  # G2
        "CLK1_M2C_N"      : "P9",   # G3
        "LA00_CC_P"       : "AE5",  # G6
        "LA00_CC_N"       : "AF5",  # G7
        "LA03_P"          : "AH1",  # G9
        "LA03_N"          : "AJ1",  # G10
        "LA08_P"          : "AE3",  # G12
        "LA08_N"          : "AF3",  # G13
        "LA12_P"          : "AD7",  # G15
        "LA12_N"          : "AD6",  # G16
        "LA16_P"          : "AG10", # G18
        "LA16_N"          : "AG9",  # G19
        "LA20_P"          : "AB11", # G21
        "LA20_N"          : "AB10", # G22
        "LA22_P"          : "AF11", # G24
        "LA22_N"          : "AG11", # G25
        "LA25_P"          : "AE10", # G27
        "LA25_N"          : "AF10", # G28
        "LA29_P"          : "W12",  # G30
        "LA29_N"          : "W11",  # G31
        "CLK0_M2C_P"      : "AE7",  # H4
        "CLK0_M2C_N"      : "AF7",  # H5
        "LA02_P"          : "AD2",  # H7
        "LA02_N"          : "AD1",  # H8
        "LA04_P"          : "AF2",  # H10
        "LA04_N"          : "AF1",  # H11
        "LA07_P"          : "AD4",  # H13
        "LA07_N"          : "AE4",  # H14
        "LA11_P"          : "AE8",  # H16
        "LA11_N"          : "AF8",  # H17
        "LA15_P"          : "AD10", # H19
        "LA15_N"          : "AE9",  # H20
        "LA19_P"          : "AA11", # H22
        "LA19_N"          : "AA10", # H23
        "LA21_P"          : "AC12", # H25
        "LA21_N"          : "AC11", # H26
        "LA24_P"          : "AH12", # H28
        "LA24_N"          : "AH11", # H29
        "LA28_P"          : "T13",  # H31
        "LA28_N"          : "R13",  # H32
    }),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxUSPPlatform):
    default_clk_name   = "clk125"
    default_clk_period = 1e9/125e6

    def __init__(self, toolchain="vivado"):
        XilinxUSPPlatform.__init__(self, "xczu9eg-ffvb1156-2-i", _io, _connectors, toolchain=toolchain)

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxUSPPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk125", loose=True), 1e9/125e6)
        self.add_period_constraint(self.lookup_request("clk300", loose=True), 1e9/300e6)
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 64]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 65]")
