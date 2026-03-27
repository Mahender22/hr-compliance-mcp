from .models import (DiscriminationProtections, BackgroundCheckLaw, DrugTestingRules, NonCompeteRules, WorkplaceSafety)

SUPPORTED_STATES = {"CA", "NY", "CO", "WA", "MA", "IL", "NJ", "OR"}

DISCRIMINATION_DATA = {
    "CA": DiscriminationProtections(state="CA", state_name="California",
        protected_classes=["Sexual orientation", "Gender identity", "Gender expression", "Marital status", "Medical condition", "Military/veteran status", "Political activities", "Reproductive health decisions", "Ancestry", "Genetic information", "Citizenship status", "Primary language", "Immigration status", "Age (40+)"],
        enforcing_agency="California Civil Rights Department (CRD, formerly DFEH)",
        notes="FEHA covers employers with 5+ employees. Broadest protections in the US."),
    "NY": DiscriminationProtections(state="NY", state_name="New York",
        protected_classes=["Sexual orientation", "Gender identity", "Gender expression", "Marital status", "Military status", "Domestic violence victim status", "Familial status", "Arrest/conviction record", "Genetic characteristics", "Citizenship/immigration status", "Reproductive health decisions", "Age (18+)", "Predisposing genetic characteristics"],
        enforcing_agency="NY Division of Human Rights",
        notes="NY Human Rights Law covers employers with 4+ employees. NYC adds additional local protections."),
    "CO": DiscriminationProtections(state="CO", state_name="Colorado",
        protected_classes=["Sexual orientation", "Gender identity", "Gender expression", "Marital status", "Ancestry", "Lawful off-duty activities", "Genetic information", "Mental/physical disability", "Age (40+)"],
        enforcing_agency="Colorado Civil Rights Division (CCRD)",
        notes="Colorado Anti-Discrimination Act (CADA). Covers all employers."),
    "WA": DiscriminationProtections(state="WA", state_name="Washington",
        protected_classes=["Sexual orientation", "Gender identity", "Marital status", "Veteran/military status", "Genetic information", "Citizenship/immigration status", "HIV/Hepatitis C status", "Off-duty tobacco use", "Age (40+)"],
        enforcing_agency="Washington State Human Rights Commission",
        notes="WA Law Against Discrimination (WLAD). Covers employers with 8+ employees."),
    "MA": DiscriminationProtections(state="MA", state_name="Massachusetts",
        protected_classes=["Sexual orientation", "Gender identity", "Marital status", "Veteran status", "Ancestry", "Genetic information", "Criminal record (CORI limits)", "Mental/physical disability", "Age (40+)"],
        enforcing_agency="Massachusetts Commission Against Discrimination (MCAD)",
        notes="MA Fair Employment Practices Act. Covers employers with 6+ employees."),
    "IL": DiscriminationProtections(state="IL", state_name="Illinois",
        protected_classes=["Sexual orientation", "Gender identity", "Marital status", "Military status", "Ancestry", "Arrest record", "Conviction record (limited)", "Order of protection status", "Unfavorable military discharge", "Citizenship status", "Genetic information", "Age (40+)"],
        enforcing_agency="Illinois Department of Human Rights (IDHR)",
        notes="IL Human Rights Act. Covers all employers (1+ employees for some protections)."),
    "NJ": DiscriminationProtections(state="NJ", state_name="New Jersey",
        protected_classes=["Sexual orientation", "Gender identity", "Gender expression", "Marital status", "Domestic partnership status", "Military service", "Ancestry", "Atypical cellular blood trait", "Genetic information", "Nationality", "Age (18-70)", "Pregnancy/breastfeeding", "Liability for military service"],
        enforcing_agency="NJ Division on Civil Rights",
        notes="NJ Law Against Discrimination (LAD). Covers all employers. One of the broadest state laws."),
    "OR": DiscriminationProtections(state="OR", state_name="Oregon",
        protected_classes=["Sexual orientation", "Gender identity", "Marital status", "Veteran status", "Family relationship", "Genetic information", "Domestic violence victim status", "Expunged juvenile record", "Age (18+)", "Credit history (limited)"],
        enforcing_agency="Oregon Bureau of Labor & Industries (BOLI)",
        notes="OR Equality Act. Covers employers with 1+ employees."),
}

BACKGROUND_CHECK_DATA = {
    "CA": BackgroundCheckLaw(state="CA", state_name="California", ban_the_box=True, fair_chance=True,
        restrictions="Cannot ask about criminal history on initial application. After conditional offer: individualized assessment required. Cannot consider convictions older than 7 years. Cannot consider arrests not leading to conviction.",
        effective_date="2018-01-01", notes="CA Fair Chance Act (AB 1008). Applies to employers with 5+ employees."),
    "NY": BackgroundCheckLaw(state="NY", state_name="New York", ban_the_box=True, fair_chance=True,
        restrictions="Cannot inquire about criminal history until after conditional offer. Must provide Article 23-A analysis. NYC: also cannot inquire about pending arrests. Cannot consider sealed/youthful offender records.",
        effective_date="2015-01-01", notes="NY Correction Law Article 23-A + NYC Fair Chance Act. NYC law among strictest in US."),
    "CO": BackgroundCheckLaw(state="CO", state_name="Colorado", ban_the_box=True, fair_chance=True,
        restrictions="Cannot ask about criminal history on initial application. Employers with 11+ employees. Cannot consider sealed/expunged records.",
        effective_date="2012-08-10", notes="Colorado Chance to Compete Act (Ban the Box). Public and private employers."),
    "WA": BackgroundCheckLaw(state="WA", state_name="Washington", ban_the_box=True, fair_chance=True,
        restrictions="Cannot ask about criminal record on application. Cannot advertise that applicants with criminal records will not be considered. Must make individualized assessment after conditional offer.",
        effective_date="2018-06-07", notes="WA Fair Chance Act. Applies to all employers."),
    "MA": BackgroundCheckLaw(state="MA", state_name="Massachusetts", ban_the_box=True, fair_chance=True,
        restrictions="Cannot ask about criminal history on application. Can only consider convictions within past 3 years (misdemeanors) or 7 years (felonies). Cannot consider sealed/expunged records.",
        effective_date="2010-11-04", notes="MA CORI Reform Act. Among the most restrictive in the US."),
    "IL": BackgroundCheckLaw(state="IL", state_name="Illinois", ban_the_box=True, fair_chance=True,
        restrictions="Cannot ask about criminal history until after interview or conditional offer. Must conduct individualized assessment using Green factors. Cannot consider sealed/expunged records.",
        effective_date="2015-01-01", notes="IL Job Opportunities for Qualified Applicants Act. Applies to employers with 15+ employees."),
    "NJ": BackgroundCheckLaw(state="NJ", state_name="New Jersey", ban_the_box=True, fair_chance=True,
        restrictions="Cannot inquire about criminal history during initial application process. Must wait until after first interview. Applies to employers with 15+ employees.",
        effective_date="2015-03-01", notes="NJ Opportunity to Compete Act (OTCA). Covers most private employers."),
    "OR": BackgroundCheckLaw(state="OR", state_name="Oregon", ban_the_box=True, fair_chance=True,
        restrictions="Cannot inquire about criminal history on initial application or before initial interview. Cannot consider expunged convictions. Cannot consider arrests not leading to conviction.",
        effective_date="2016-01-01", notes="OR Ban the Box Law. Applies to all employers."),
}

DRUG_TESTING_DATA = {
    "CA": DrugTestingRules(state="CA", state_name="California",
        pre_employment="Generally permitted, but cannot test for marijuana use off-duty (AB 2188, effective 2024)",
        random_testing="Only permitted for safety-sensitive positions or federal mandates",
        marijuana_protections="Cannot discriminate based on off-duty marijuana use. Cannot use hair follicle test for marijuana. Applies to most employers with 5+ employees.",
        notes="AB 2188 (2024): strongest marijuana employment protections in US."),
    "NY": DrugTestingRules(state="NY", state_name="New York",
        pre_employment="Cannot test for marijuana. Other drugs: generally permitted",
        random_testing="Cannot test for marijuana (except safety-sensitive, DOT-regulated). Other drugs: limited",
        marijuana_protections="NY MRTA: cannot test for marijuana or discriminate based on legal marijuana use. Exceptions: safety-sensitive jobs, federal contracts, impairment on the job.",
        notes="Strong marijuana protections since MRTA (2021)."),
    "CO": DrugTestingRules(state="CO", state_name="Colorado",
        pre_employment="Permitted. Marijuana: employer may still test and make decisions based on results",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="Limited. Despite legal recreational marijuana, employers can still test and terminate for marijuana use. No off-duty use protections for marijuana (unlike tobacco)."),
    "WA": DrugTestingRules(state="WA", state_name="Washington",
        pre_employment="Permitted. Some restrictions on marijuana testing",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="Cannot discriminate based on off-duty marijuana use (2024 law). Exceptions: safety-sensitive, federal requirements, impairment.",
        notes="Protections for off-duty marijuana use added in 2024."),
    "MA": DrugTestingRules(state="MA", state_name="Massachusetts",
        pre_employment="Permitted but cannot be sole basis for denial if marijuana-positive",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="Employers cannot penalize for off-duty recreational marijuana use. Must provide reasonable accommodation for medical marijuana (case law, Barbuto v. Advantage Sales)."),
    "IL": DrugTestingRules(state="IL", state_name="Illinois",
        pre_employment="Permitted. May test for marijuana but cannot take adverse action for off-duty use",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="Cannabis Regulation and Tax Act: employers may have drug-free workplace policies but cannot penalize for lawful off-duty use. Must have good-faith belief of impairment for adverse action.",
        notes="Must have good-faith belief of on-the-job impairment before taking action."),
    "NJ": DrugTestingRules(state="NJ", state_name="New Jersey",
        pre_employment="Permitted but cannot take adverse action solely for positive marijuana test",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="NJ CREAMMA: cannot refuse to hire or fire solely for positive marijuana test. Requires workplace impairment recognition expert (WIRE) for impairment-based actions.",
        notes="Unique WIRE (Workplace Impairment Recognition Expert) requirement."),
    "OR": DrugTestingRules(state="OR", state_name="Oregon",
        pre_employment="Permitted. Marijuana: employer may still test",
        random_testing="Permitted for safety-sensitive positions",
        marijuana_protections="No specific off-duty marijuana employment protections. Employers may test and make employment decisions based on results despite legal recreational use.",
        notes="Oregon has not enacted employment protections for marijuana use."),
}

NONCOMPETE_DATA = {
    "CA": NonCompeteRules(state="CA", state_name="California", enforceable=False,
        restrictions="Non-competes are void and unenforceable under Bus. & Prof. Code 16600. Employer cannot even require employee to sign one. AB 1076 (2024): void even if signed in another state.",
        effective_date="1872", notes="Broadest non-compete ban in the US. Narrowly allows non-solicitation of trade secrets."),
    "NY": NonCompeteRules(state="NY", state_name="New York", enforceable=True,
        restrictions="Enforceable if reasonable in scope, duration (typically 1-2 years max), and geography. Must protect legitimate business interest. Consideration required for existing employees.",
        notes="No comprehensive ban yet despite legislative attempts. Courts apply reasonableness test."),
    "CO": NonCompeteRules(state="CO", state_name="Colorado", enforceable=True,
        restrictions="Only enforceable for workers earning above threshold ($123,750/yr in 2025, adjusted annually). Non-solicitation: above $49,500/yr. Must be part of agreement with additional consideration.",
        income_threshold="$123,750/year (adjusted annually for CPI)", effective_date="2022-08-10",
        notes="HB 22-1317. Must disclose terms to worker before accepting the job. Penalties up to $5,000 per violation."),
    "WA": NonCompeteRules(state="WA", state_name="Washington", enforceable=True,
        restrictions="Only enforceable for employees earning $116,594+/yr or independent contractors earning $291,486+/yr (2025, adjusted annually). Max 18 months. Must be disclosed at or before acceptance of employment.",
        income_threshold="$116,594/year (employees), $291,486/year (contractors)", effective_date="2020-01-01",
        notes="Among the most protective statutes. Employer must pay garden leave during restriction period."),
    "MA": NonCompeteRules(state="MA", state_name="Massachusetts", enforceable=True,
        restrictions="Max 12 months. Cannot apply to non-exempt workers, laid-off employees, or employees terminated without cause. Must provide garden leave pay (50% base salary) OR other mutually agreed consideration.",
        income_threshold="Must be exempt employee", effective_date="2018-10-01",
        notes="MA Non-Competition Agreement Act. Must be presented at hiring or with garden leave consideration."),
    "IL": NonCompeteRules(state="IL", state_name="Illinois", enforceable=True,
        restrictions="Non-competes: only for employees earning $75,000+/yr. Non-solicitation: $45,000+/yr. Must have adequate consideration (2 years of employment or other consideration).",
        income_threshold="$75,000/year (non-compete), $45,000/year (non-solicitation)", effective_date="2022-01-01",
        notes="IL Freedom to Work Act. Employer must advise employee to consult attorney; 14-day review period required."),
    "NJ": NonCompeteRules(state="NJ", state_name="New Jersey", enforceable=True,
        restrictions="Enforceable if reasonable in scope, duration, and geography. Courts apply a fact-specific reasonableness analysis. Typically 1-2 years max. Must protect legitimate business interest.",
        notes="No comprehensive statute. Governed by common law reasonableness test."),
    "OR": NonCompeteRules(state="OR", state_name="Oregon", enforceable=True,
        restrictions="Only enforceable for employees earning above median household income ($100,533/yr in 2024). Max 12 months. Must be in writing, signed at hire or with promotion/raise.",
        income_threshold="$100,533/year (median household income, adjusted)", effective_date="2021-01-01",
        notes="ORS 653.295. Recent amendments significantly restricted enforceability."),
}

WORKPLACE_SAFETY_DATA = {
    "CA": WorkplaceSafety(state="CA", state_name="California", has_state_plan=True,
        agency="Cal/OSHA (Division of Occupational Safety & Health)",
        unique_requirements="Heat illness prevention (outdoor + indoor), workplace violence prevention plan (SB 553, 2024), injury & illness prevention program (IIPP) required for all employers, wildfire smoke protection.",
        notes="Cal/OSHA standards often exceed federal OSHA. Covers public and private sector."),
    "NY": WorkplaceSafety(state="NY", state_name="New York", has_state_plan=True,
        agency="NY PESH (Public Employee Safety & Health)",
        unique_requirements="State plan covers public sector only. Private sector covered by federal OSHA. NY HERO Act (2021): airborne infectious disease prevention plans required. Retail Worker Safety Act (2025): panic buttons.",
        notes="Split jurisdiction: PESH for public employees, federal OSHA for private."),
    "WA": WorkplaceSafety(state="WA", state_name="Washington", has_state_plan=True,
        agency="WA L&I DOSH (Division of Occupational Safety & Health)",
        unique_requirements="Heat-related illness rules (agricultural and outdoor), wildfire smoke (WAC 296-62-085), violence in healthcare settings.",
        notes="Covers both public and private sector. Often stricter than federal OSHA."),
    "OR": WorkplaceSafety(state="OR", state_name="Oregon", has_state_plan=True,
        agency="Oregon OSHA",
        unique_requirements="Heat illness prevention (OR-OSHA heat rule is among strictest — triggers at 80F), wildfire smoke protection, agricultural safety standards beyond federal, workplace violence prevention.",
        notes="Oregon OSHA covers both public and private sector."),
    "CO": WorkplaceSafety(state="CO", state_name="Colorado", has_state_plan=False,
        agency="Federal OSHA (no state plan)",
        unique_requirements="No state OSHA plan — covered by federal OSHA. COMPS Order adds wage/hour safety requirements. Public Health Emergency Whistleblower Act protects employees reporting unsafe conditions."),
    "MA": WorkplaceSafety(state="MA", state_name="Massachusetts", has_state_plan=False,
        agency="Federal OSHA (no state plan for private sector)",
        unique_requirements="No state OSHA plan for private sector. State covers public employees only. Workplace violence prevention in healthcare facilities required.",
        notes="Private sector covered exclusively by federal OSHA."),
    "IL": WorkplaceSafety(state="IL", state_name="Illinois", has_state_plan=False,
        agency="Federal OSHA (no state plan for private sector)",
        unique_requirements="No state plan for private sector. IL OSHA covers state and local government employees only. Day and Temporary Labor Services Act adds protections for temp workers."),
    "NJ": WorkplaceSafety(state="NJ", state_name="New Jersey", has_state_plan=True,
        agency="NJ PEOSH (Public Employees Occupational Safety & Health)",
        unique_requirements="State plan covers public employees only. Private sector: federal OSHA. Indoor air quality standards for public buildings. Right to Know Act (one of first in US).",
        notes="Split jurisdiction similar to NY."),
}


def _validate_state(state: str) -> str:
    state = state.upper()
    if state not in SUPPORTED_STATES:
        supported = ", ".join(sorted(SUPPORTED_STATES))
        raise ValueError(f"State '{state}' not supported. Supported states: {supported}")
    return state

def get_discrimination_protections(state: str) -> DiscriminationProtections:
    return DISCRIMINATION_DATA[_validate_state(state)]

def get_background_check_laws(state: str) -> BackgroundCheckLaw:
    return BACKGROUND_CHECK_DATA[_validate_state(state)]

def get_drug_testing_rules(state: str) -> DrugTestingRules:
    return DRUG_TESTING_DATA[_validate_state(state)]

def get_noncompete_rules(state: str) -> NonCompeteRules:
    return NONCOMPETE_DATA[_validate_state(state)]

def get_workplace_safety(state: str) -> WorkplaceSafety:
    return WORKPLACE_SAFETY_DATA[_validate_state(state)]
