from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional


class MilestoneType(Enum):
    TRIAL_PCD = "Trial Primary Completion"
    TRIAL_READOUT = "Trial Data Readout"
    FDA_SUBMISSION = "FDA Submission"
    FDA_APPROVAL = "FDA Approval"
    EMA_APPROVAL = "EMA Approval"
    MHRA_APPROVAL = "MHRA Approval"
    HEALTH_CANADA_APPROVAL = "Health Canada Approval"
    NCCN_GUIDELINE = "NCCN Guideline Inclusion"
    ESMO_GUIDELINE = "ESMO Guideline Inclusion"
    NICE_DECISION = "NICE Final Appraisal"
    GBA_DECISION = "G-BA Benefit Assessment"
    HAS_DECISION = "HAS Transparency Committee"
    AIFA_DECISION = "AIFA Reimbursement"
    AEMPS_DECISION = "AEMPS Pricing & Reimbursement"
    CADTH_DECISION = "CADTH Recommendation"
    COMMERCIAL_LAUNCH = "Commercial Launch"
    SOC_INTEGRATION = "SoC Integration"


class Confidence(Enum):
    KNOWN = "Known"
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"
    GAP = "Gap"


class Market(Enum):
    US = "US"
    UK = "UK"
    FR = "France"
    DE = "Germany"
    IT = "Italy"
    ES = "Spain"
    CA = "Canada"


MARKETS = list(Market)

# Which regulatory milestone applies to each market
REGULATORY_MILESTONE = {
    Market.US: MilestoneType.FDA_APPROVAL,
    Market.UK: MilestoneType.MHRA_APPROVAL,
    Market.FR: MilestoneType.EMA_APPROVAL,
    Market.DE: MilestoneType.EMA_APPROVAL,
    Market.IT: MilestoneType.EMA_APPROVAL,
    Market.ES: MilestoneType.EMA_APPROVAL,
    Market.CA: MilestoneType.HEALTH_CANADA_APPROVAL,
}

# Which HTA/reimbursement milestone applies to each market
HTA_MILESTONE = {
    Market.US: None,  # No formal HTA gate in US
    Market.UK: MilestoneType.NICE_DECISION,
    Market.FR: MilestoneType.HAS_DECISION,
    Market.DE: MilestoneType.GBA_DECISION,
    Market.IT: MilestoneType.AIFA_DECISION,
    Market.ES: MilestoneType.AEMPS_DECISION,
    Market.CA: MilestoneType.CADTH_DECISION,
}

# Which guideline body applies
GUIDELINE_MILESTONE = {
    Market.US: MilestoneType.NCCN_GUIDELINE,
    Market.UK: MilestoneType.ESMO_GUIDELINE,
    Market.FR: MilestoneType.ESMO_GUIDELINE,
    Market.DE: MilestoneType.ESMO_GUIDELINE,
    Market.IT: MilestoneType.ESMO_GUIDELINE,
    Market.ES: MilestoneType.ESMO_GUIDELINE,
    Market.CA: MilestoneType.NCCN_GUIDELINE,
}

# HTA body names for display
HTA_BODY_NAMES = {
    Market.US: "N/A (Commercial)",
    Market.UK: "NICE",
    Market.FR: "HAS (Transparency Committee)",
    Market.DE: "G-BA (AMNOG)",
    Market.IT: "AIFA",
    Market.ES: "AEMPS / IPT",
    Market.CA: "CADTH / pCODR",
}


@dataclass
class Milestone:
    milestone_type: MilestoneType
    market: Market
    date_value: Optional[date]
    confidence: Confidence
    source: str
    notes: str = ""
    source_url: Optional[str] = None
    is_projected: bool = False


@dataclass
class DrugProgram:
    drug_name: str
    indication: str
    trial_name: str
    sponsor: str
    milestones: list[Milestone] = field(default_factory=list)

    def get_milestone(self, mtype: MilestoneType, market: Market) -> Optional[Milestone]:
        for m in self.milestones:
            if m.milestone_type == mtype and m.market == market:
                return m
        return None

    def get_fda_approval_date(self) -> Optional[date]:
        m = self.get_milestone(MilestoneType.FDA_APPROVAL, Market.US)
        return m.date_value if m else None

    def add_milestone(self, milestone: Milestone):
        # Replace existing if same type+market
        self.milestones = [
            m for m in self.milestones
            if not (m.milestone_type == milestone.milestone_type and m.market == milestone.market)
        ]
        self.milestones.append(milestone)


@dataclass
class AnalogLag:
    analog_name: str
    milestone_type: MilestoneType
    market: Market
    lag_months: Optional[float]
    source: str


@dataclass
class Assumption:
    id: str
    category: str
    description: str
    impact: str  # "High", "Medium", "Low"
    status: str  # "Active", "Resolved"
    related_drug: Optional[str] = None
    gap_flag: bool = False
