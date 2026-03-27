from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MinimumWage:
    state: str
    state_name: str
    minimum_wage: float
    tipped_wage: float
    tip_credit: bool
    effective_date: str
    notes: str = ""
    scheduled_increases: list = field(default_factory=list)
    local_rates: list = field(default_factory=list)

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items() if v is not None and v != ""}
        if not self.scheduled_increases:
            d.pop("scheduled_increases", None)
        if not self.local_rates:
            d.pop("local_rates", None)
        return d


@dataclass
class OvertimeRules:
    state: str
    state_name: str
    weekly_threshold: int
    weekly_rate: float
    daily_threshold: Optional[int] = None
    daily_rate: Optional[float] = None
    exemptions: list = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items() if v is not None}
        if not self.exemptions:
            d.pop("exemptions", None)
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class PayFrequency:
    state: str
    state_name: str
    frequency: str
    details: str
    exceptions: str = ""

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v}


@dataclass
class PayTransparency:
    state: str
    state_name: str
    requires_posting: bool
    requires_on_request: bool
    effective_date: str
    employer_threshold: Optional[int] = None
    details: str = ""
    penalties: str = ""

    def to_dict(self) -> dict:
        d = {}
        for k, v in self.__dict__.items():
            if v is None:
                continue
            if isinstance(v, str) and v == "":
                continue
            d[k] = v
        return d


@dataclass
class PaidSickLeave:
    state: str
    state_name: str
    mandated: bool
    accrual_rate: str
    max_annual: str
    max_carryover: str
    eligibility: str
    effective_date: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class FamilyLeave:
    state: str
    state_name: str
    has_program: bool
    program_name: str
    duration: str
    wage_replacement: str
    eligibility: str
    effective_date: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class VacationPayout:
    state: str
    state_name: str
    required: bool
    conditions: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class VotingLeave:
    state: str
    state_name: str
    required: bool
    paid: bool
    duration: str
    notice_required: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class BereavementLeave:
    state: str
    state_name: str
    mandated: bool
    duration: str
    qualifying_relationships: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class DiscriminationProtections:
    state: str
    state_name: str
    protected_classes: list
    enforcing_agency: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class BackgroundCheckLaw:
    state: str
    state_name: str
    ban_the_box: bool
    fair_chance: bool
    restrictions: str
    effective_date: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class DrugTestingRules:
    state: str
    state_name: str
    pre_employment: str
    random_testing: str
    marijuana_protections: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class NonCompeteRules:
    state: str
    state_name: str
    enforceable: bool
    restrictions: str
    income_threshold: str = ""
    effective_date: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None and v != ""}


@dataclass
class WorkplaceSafety:
    state: str
    state_name: str
    has_state_plan: bool
    agency: str
    unique_requirements: str
    notes: str = ""

    def to_dict(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        if not self.notes:
            d.pop("notes", None)
        return d


@dataclass
class LawChange:
    state: str
    state_name: str
    category: str
    description: str
    effective_date: str
    impact: str

    def to_dict(self) -> dict:
        return self.__dict__.copy()
