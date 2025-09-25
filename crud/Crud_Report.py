

# 	report.py → Operações de relatórios.
from crud.baseAsync import CRUDBase
from models.model_report import Report
from schemas.schema_report import ReportCreate, ReportUpdate


class CRUDItem(CRUDBase[Report, ReportCreate, ReportUpdate]):
    pass


report_crud = CRUDItem(Report)
