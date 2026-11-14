<div dir="rtl">

> **الوثيقة:** مخططات حالات الاستخدام (Use Case Diagrams) — **النظام:** OptiTime — **التاريخ:** 2026-10-15

# مخططات حالات الاستخدام — نظام OptiTime

تضم هذه الوثيقة أكواد PlantUML لثمانية عشر مخطط حالات استخدام: مخطط عام للنظام، ومخطط لكل حزمة من الحزم السبع عشرة في ملف السيناريوهات (`UseCase Scenario/optitime-usecase-scenarios.md`). وتطابق المخططاتُ السيناريوهاتِ في أرقام الحالات وأسمائها وفاعليها وحزمها، وفي علاقات التضمين (include) والتوسيع (extend) المذكورة فيها. وتحافظ مخططات الحزم الثلاث الأولى على بنية مخططات الفريق الأولى (Auth_profile وUser and Roles وResources)، مع إضافة الحالتين UC-08 وUC-25.

**الملفات:** كود كل مخطط في مجلد `Src` (مثل `Src/UCD-01-auth.puml`)، وصورته المولّدة في مجلد `Images` بالاسم نفسه (مثل `Images/UCD-01-auth.png`)؛ والأسماء من UCD-00 إلى UCD-06 هي التي حجزتها وثيقة متطلبات البرمجيات لهذه المخططات. والكود في هذه الوثيقة مطابق حرفياً لملفات `Src`.

## طريقة العرض والتصدير

1. **الصور الجاهزة:** في مجلد `Images` بدقة 150 نقطة في البوصة، صالحة للطباعة مباشرة، وهي معروضة أيضاً تحت كل مخطط في هذه الوثيقة.
2. **ملف `.puml` منفرد:** افتح أي ملف من مجلد `Src` في VS Code واضغط Alt+D للمعاينة، ثم صدّره من قائمة الأوامر (Ctrl+Shift+P) بالأمر «PlantUML: Export Current Diagram» بصيغة PNG أو SVG. ويعمل ذلك بـ Java وحدها دون إنترنت.
3. **معاينة Markdown:** تعرض إضافة PlantUML (`jebbs.plantuml`) كتل الكود في هذه الوثيقة عبر خادم PlantUML يُحدَّد في الإعداد `plantuml.server`، كما في وثيقتي مخططات التسلسل والنشاط.

كل كتلة مكتفية بذاتها: تبدأ بالنمط الموحّد (أسطر `skinparam`) ثم الفاعلين وحالات الاستخدام والعلاقات، واسم المخطط بعد كلمة `startuml` هو اسم ملف الصورة عند التصدير.

## دليل الرموز

| العنصر في المخطط | معناه |
|---|---|
| شكل الشخص | فاعل: دور في النظام برمزه (مثل ADM) أو جهة خارجية |
| شكل بيضوي | حالة استخدام، ورقمها تحت اسمها |
| شكل بيضوي دون رقم | حالة جامعة تتفرع منها حالات أخرى (مثل «إدارة الملف الشخصي») |
| شكل بيضوي رمادي بإطار متقطع | حالة من حزمة أخرى تظهر لعلاقة تربطها بحالة من الحزمة، واسم حزمتها ورقمها تحت اسمها |
| إطار بعنوان | حدود الحزمة، أو حدود النظام في المخطط العام |
| خط متصل | الفاعل يشارك في حالة الاستخدام |
| سهم متقطع «include» | الحالة الأساسية تتضمن الحالة المشار إليها في كل مرة |
| سهم متقطع «extend» | الحالة توسّع الحالة المشار إليها عند شرط أو اختيار |
| عبارة «عرض فقط» على خط | الفاعل يطّلع دون تعديل |
| مستطيل أصفر بزاوية | ملاحظة |

## فهرس المخططات

| الرقم | المخطط | الحالات | الفاعلون | الصورة | الكود |
|---|---|---|---|---|---|
| UCD-00 | المخطط العام للنظام | UC-01 … UC-113 | جميع الأدوار والجهات الخارجية | `Images/UCD-00-overview.png` | `Src/UCD-00-overview.puml` |
| UCD-01 | حزمة المصادقة والملف الشخصي (Auth and Profile) | UC-01 … UC-08 | المستخدم (أي دور)، وخدمة المصادقة | `Images/UCD-01-auth.png` | `Src/UCD-01-auth.puml` |
| UCD-02 | حزمة المستخدمين والأدوار (Users and Roles) | UC-09 … UC-17 | ADM، وEXE (عرض فقط) | `Images/UCD-02-users.png` | `Src/UCD-02-users.puml` |
| UCD-03 | حزمة الموارد (Resources) | UC-18 … UC-26 | CRD، وINS، وEMP، وLIB | `Images/UCD-03-resources.png` | `Src/UCD-03-resources.puml` |
| UCD-04 | حزمة الجدولة (Scheduling) | UC-27 … UC-33 | INS، وCRD، وHOD، وDEN، وACO، وSTU | `Images/UCD-04-scheduling.png` | `Src/UCD-04-scheduling.puml` |
| UCD-05 | حزمة الامتحانات والدرجات (Exams and Grades) | UC-34 … UC-35 | EXM، وSTU | `Images/UCD-05-grades.png` | `Src/UCD-05-grades.puml` |
| UCD-06 | حزمة التقويم والتقارير والنظام (Calendar, Reports and System) | UC-36 … UC-38 | ACO، وEXE، وADM | `Images/UCD-06-system.png` | `Src/UCD-06-system.puml` |
| UCD-07 | حزمة الإدارة والمتابعة (Administration and Monitoring) | UC-39 … UC-47 | ADM، والمستخدم (أي دور)، وCRD، وACO، ونظام خارجي، وخدمة الإشعارات الفورية | `Images/UCD-07-admin.png` | `Src/UCD-07-admin.puml` |
| UCD-08 | حزمة الهيكل الأكاديمي والخطط (Academic Structure and Plans) | UC-48 … UC-56 | ADM، وDEN، وACO، وCRD | `Images/UCD-08-structure.png` | `Src/UCD-08-structure.puml` |
| UCD-09 | حزمة إعداد الجدولة وتشغيلها (Scheduling Preparation and Operations) | UC-57 … UC-62 | CRD، وADM، وACO، وDEN، وHOD، وINS | `Images/UCD-09-scheduling-ops.png` | `Src/UCD-09-scheduling-ops.puml` |
| UCD-10 | حزمة سجلات الطلاب والتسجيل (Student Records and Registration) | UC-63 … UC-71 | STU، وADM، وADO، وACO، وADV | `Images/UCD-10-registration.png` | `Src/UCD-10-registration.puml` |
| UCD-11 | حزمة الحضور والتعلّم والتقييم (Attendance, Learning and Evaluation) | UC-72 … UC-77 | INS، وSTU، وACO، وHOD، وDEN | `Images/UCD-11-learning.png` | `Src/UCD-11-learning.puml` |
| UCD-12 | حزمة سير اعتماد الدرجات (Grade Approval Workflow) | UC-78 … UC-83 | INS، وHOD، وEXM، وDEN، وSTU، وACO | `Images/UCD-12-grades-workflow.png` | `Src/UCD-12-grades-workflow.puml` |
| UCD-13 | حزمة جدولة الامتحانات وتنفيذها (Exam Scheduling and Operations) | UC-84 … UC-87 | EXM، وINS (مراقباً)، وSTU | `Images/UCD-13-exams.png` | `Src/UCD-13-exams.puml` |
| UCD-14 | حزمة القبول والإرشاد (Admission and Advising) | UC-88 … UC-92 | ADO، وAPL، وبوابة الدفع الإلكتروني، وADV، وSTU | `Images/UCD-14-admission-advising.png` | `Src/UCD-14-admission-advising.puml` |
| UCD-15 | حزمة المالية (Finance) | UC-93 … UC-96 | FIN، وSTU، وبوابة الدفع الإلكتروني | `Images/UCD-15-finance.png` | `Src/UCD-15-finance.puml` |
| UCD-16 | حزمة المكتبة وشؤون الموظفين والطلبات (Library, Staff Affairs and E-Requests) | UC-97 … UC-103 | STU، وINS، وLIB، وHRO، وEMP، وجهاز البصمة، والمدير المباشر، وACO، وEXM | `Images/UCD-16-services.png` | `Src/UCD-16-services.puml` |
| UCD-17 | حزمة الذكاء الاصطناعي والتحليلات (AI and Analytics) | UC-104 … UC-113 | ADM، وEXE، وCRD، وINS، والمستخدم (أي دور)، وACO، وADV، وHOD، ومزوّد النماذج اللغوية | `Images/UCD-17-ai.png` | `Src/UCD-17-ai.puml` |

---

## UCD-00: المخطط العام للنظام

**الحالات:** UC-01 … UC-113. **الفاعلون:** جميع الأدوار والجهات الخارجية. **يوضّح المخطط:** حدود النظام وحزمه السبع عشرة، ولكل حزمة مجال حالاتها، والفاعلين الرئيسيين في كل حزمة. ويرث كل دور حالات «المصادقة والملف الشخصي» لأنه مستخدم للنظام، ويطّلع EXE على المستخدمين والأدوار للعرض فقط. وارتباطات كل فاعل بحالات الحزمة كاملةٌ في مخطط الحزمة نفسها.

![UCD-00-overview: المخطط العام للنظام](Images/UCD-00-overview.png)

<div dir="ltr">

```plantuml
@startuml UCD-00-overview
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam rectangle {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
skinparam note {
  BackgroundColor #FFF8E1
  BorderColor #FFB300
  FontSize 12
}
left to right direction
' ===== المخطط =====

actor "الإدارة العليا\nEXE" as EXE
actor "موظف القبول\nADO" as ADO
actor "مدير النظام\nADM" as ADM
actor "عميد الكلية\nDEN" as DEN
actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "موظف شؤون\nالامتحانات\nEXM" as EXM
actor "رئيس القسم\nHOD" as HOD
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "أمين المكتبة\nLIB" as LIB
actor "الموظف المالي\nFIN" as FIN
actor "موظف شؤون\nالموظفين\nHRO" as HRO

actor "خدمة المصادقة\nAuth Service" as AUTH
actor "المستخدم\nAny User" as USER
actor "مزوّد النماذج\nاللغوية\nLLM Provider" as LLM
actor "خدمة الإشعارات\nالفورية\nFCM" as FCM
actor "نظام خارجي\nExternal System" as EXT
actor "عضو هيئة التدريس\nINS" as INS
actor "الطالب\nSTU" as STU
actor "المرشد الأكاديمي\nADV" as ADV
actor "المتقدّم\nAPL" as APL
actor "بوابة الدفع\nالإلكتروني\nPayment Gateway" as PG
actor "موظف\nEMP" as EMP
actor "جهاز البصمة" as BIO

rectangle "OptiTime" {
  usecase "المستخدمون والأدوار\nUC-09 … UC-17" as P2
  usecase "المصادقة والملف الشخصي\nUC-01 … UC-08" as P1
  usecase "الذكاء الاصطناعي والتحليلات\nUC-104 … UC-113" as P17
  usecase "التقويم والتقارير والنظام\nUC-36 … UC-38" as P6
  usecase "الإدارة والمتابعة\nUC-39 … UC-47" as P7
  usecase "الهيكل الأكاديمي والخطط\nUC-48 … UC-56" as P8
  usecase "إعداد الجدولة وتشغيلها\nUC-57 … UC-62" as P9
  usecase "الحضور والتعلّم والتقييم\nUC-72 … UC-77" as P11
  usecase "الجدولة\nUC-27 … UC-33" as P4
  usecase "سير اعتماد الدرجات\nUC-78 … UC-83" as P12
  usecase "سجلات الطلاب والتسجيل\nUC-63 … UC-71" as P10
  usecase "الامتحانات والدرجات\nUC-34 … UC-35" as P5
  usecase "جدولة الامتحانات وتنفيذها\nUC-84 … UC-87" as P13
  usecase "الموارد\nUC-18 … UC-26" as P3
  usecase "القبول والإرشاد\nUC-88 … UC-92" as P14
  usecase "المالية\nUC-93 … UC-96" as P15
  usecase "المكتبة وشؤون الموظفين\nوالطلبات\nUC-97 … UC-103" as P16
}

note right of USER
  جميع الأدوار ترث
  حالات المصادقة
  والملف الشخصي
end note

EXE -- P2 : عرض فقط
EXE -- P17
EXE -- P6
ADO -- P10
ADO -- P14
ADM -- P2
ADM -- P17
ADM -- P6
ADM -- P7
ADM -- P8
DEN -- P4
CRD -- P8
CRD -- P9
CRD -- P4
CRD -- P3
EXM -- P12
EXM -- P5
EXM -- P13
HOD -- P4
HOD -- P12
ACO -- P6
ACO -- P8
ACO -- P9
ACO -- P4
ACO -- P10
LIB -- P3
LIB -- P16
FIN -- P15
HRO -- P16

P1 -- AUTH
P1 -- USER
P17 -- USER
P7 -- USER
P17 -- LLM
P7 -- FCM
P7 -- EXT
P11 -- INS
P4 -- INS
P12 -- INS
P3 -- INS
P11 -- STU
P4 -- STU
P10 -- STU
P5 -- STU
P13 -- STU
P15 -- STU
P16 -- STU
P10 -- ADV
P14 -- ADV
P14 -- APL
P14 -- PG
P15 -- PG
P3 -- EMP
P16 -- EMP
P16 -- BIO
@enduml
```

</div>

---

## UCD-01: حزمة المصادقة والملف الشخصي (Auth and Profile)

**الحالات:** UC-01 … UC-08. **الفاعلون:** المستخدم (أي دور)، وخدمة المصادقة. **يوضّح المخطط:** الدخول والخروج وإدارة الملف الشخصي واستعادة كلمة المرور والتحقق الثنائي.

**العلاقات:**

- تتضمن «نسيت كلمة المرور» UC-05 حالة «التحقق الثنائي» UC-06، التي تتضمن بدورها «تغيير كلمة المرور» UC-07.
- توسّع حالات «عرض الملف الشخصي» UC-03 و«تعديل الملف الشخصي» UC-04 و«تغيير كلمة المرور» UC-07 و«تفعيل التحقق الثنائي» UC-08 حالة «إدارة الملف الشخصي».
- تشارك «خدمة المصادقة» في تسجيل الدخول UC-01 والتحقق الثنائي UC-06.

![UCD-01-auth: حزمة المصادقة والملف الشخصي (Auth and Profile)](Images/UCD-01-auth.png)

<div dir="ltr">

```plantuml
@startuml UCD-01-auth
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "المستخدم\nAny User" as USER
actor "خدمة المصادقة\nAuth Service" as AUTH

package "المصادقة والملف الشخصي\nAuth and Profile" {
  usecase "تسجيل الدخول\nUC-01" as UC01
  usecase "تسجيل الخروج\nUC-02" as UC02
  usecase "إدارة الملف الشخصي" as PROFILE
  usecase "عرض الملف الشخصي\nUC-03" as UC03
  usecase "تعديل الملف الشخصي\nUC-04" as UC04
  usecase "تغيير كلمة المرور\nUC-07" as UC07
  usecase "تفعيل التحقق الثنائي\nعبر تطبيق المصادقة\nUC-08" as UC08
  usecase "نسيت كلمة المرور\nUC-05" as UC05
  usecase "التحقق الثنائي\nرمز التحقق\nUC-06" as UC06
}

USER -- UC01
USER -- UC02
USER -- PROFILE
USER -- UC05

PROFILE <.. UC03 : <<extend>>
PROFILE <.. UC04 : <<extend>>
PROFILE <.. UC08 : <<extend>>
PROFILE <.. UC07 : <<extend>>
UC05 ..> UC06 : <<include>>
UC06 ..> UC07 : <<include>>

UC01 --- AUTH
UC06 -- AUTH
@enduml
```

</div>

---

## UCD-02: حزمة المستخدمين والأدوار (Users and Roles)

**الحالات:** UC-09 … UC-17. **الفاعلون:** ADM، وEXE (عرض فقط). **يوضّح المخطط:** إدارة الحسابات وأدوارها، ومصفوفة الصلاحيات، وإدارة الأدوار.

**العلاقات:**

- توسّع حالات العرض والإنشاء والتعديل والحذف (UC-09 إلى UC-12) حالة «إدارة المستخدمين»، وتوسّع حالات الأدوار (UC-15 إلى UC-17) حالة «إدارة الأدوار».
- تتضمن «إنشاء مستخدم» UC-10 حالة «تعيين الأدوار» UC-13، وتوسّع UC-13 حالة «تعديل مستخدم» UC-11.
- يطّلع EXE على قائمة المستخدمين UC-09 ومصفوفة الصلاحيات UC-14 للعرض فقط.

![UCD-02-users: حزمة المستخدمين والأدوار (Users and Roles)](Images/UCD-02-users.png)

<div dir="ltr">

```plantuml
@startuml UCD-02-users
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "مدير النظام\nADM" as ADM
actor "الإدارة العليا\nEXE" as EXE

package "المستخدمون والأدوار\nUsers and Roles" {
  usecase "إدارة المستخدمين" as USERS
  usecase "عرض المستخدمين\nUC-09" as UC09
  usecase "إنشاء مستخدم\nUC-10" as UC10
  usecase "تعديل مستخدم\nUC-11" as UC11
  usecase "حذف مستخدم\nUC-12" as UC12
  usecase "تعيين الأدوار\nUC-13" as UC13
  usecase "عرض مصفوفة الصلاحيات\nRACI · UC-14" as UC14
  usecase "إدارة الأدوار" as ROLES
  usecase "إضافة دور\nUC-15" as UC15
  usecase "تعديل دور\nUC-16" as UC16
  usecase "حذف دور\nUC-17" as UC17
}

ADM -- USERS
ADM -- UC13
ADM -- UC14
ADM -- ROLES
EXE -- UC09 : عرض فقط
EXE -- UC14 : عرض فقط

USERS <.. UC09 : <<extend>>
USERS <.. UC10 : <<extend>>
USERS <.. UC11 : <<extend>>
USERS <.. UC12 : <<extend>>
UC13 <.. UC10 : <<include>>
UC13 ..> UC11 : <<extend>>

ROLES <.. UC15 : <<extend>>
ROLES <.. UC16 : <<extend>>
ROLES <.. UC17 : <<extend>>
@enduml
```

</div>

---

## UCD-03: حزمة الموارد (Resources)

**الحالات:** UC-18 … UC-26. **الفاعلون:** CRD، وINS، وEMP، وLIB. **يوضّح المخطط:** إدارة القاعات والمختبرات والأجهزة والصيانة، وعرض الموارد وطلبها وحجز القاعات.

**العلاقات:**

- تتضمن «إدارة القاعات» UC-18 حالة «تحديد سعة الامتحان» UC-19.
- توسّع «إدارة الصيانة» UC-22 حالتي «إدارة الأجهزة» UC-20 و«إدارة المختبرات» UC-21 (الإبلاغ عن عطل).
- توسّع «طلب موارد إضافية» UC-24 و«حجز قاعة دراسية» UC-26 حالة «عرض الموارد» UC-23، ويعالج المنسق الطلبات في UC-25.

![UCD-03-resources: حزمة الموارد (Resources)](Images/UCD-03-resources.png)

<div dir="ltr">

```plantuml
@startuml UCD-03-resources
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "عضو هيئة التدريس\nINS" as INS
actor "موظف\nEMP" as EMP
actor "أمين المكتبة\nLIB" as LIB

package "الموارد\nResources" {
  usecase "إدارة القاعات\nUC-18" as UC18
  usecase "تحديد سعة الامتحان\nUC-19" as UC19
  usecase "إدارة الأجهزة\nUC-20" as UC20
  usecase "إدارة الصيانة\nUC-22" as UC22
  usecase "إدارة المختبرات\nUC-21" as UC21
  usecase "معالجة طلبات الموارد\nUC-25" as UC25
  usecase "طلب موارد إضافية\nUC-24" as UC24
  usecase "حجز قاعة دراسية\nUC-26" as UC26
  usecase "عرض الموارد\nUC-23" as UC23
}

CRD -- UC18
CRD -- UC19
CRD -- UC20
CRD -- UC22
CRD -- UC21
CRD -- UC25
UC18 .> UC19 : <<include>>
UC20 <. UC22 : <<extend>>
UC22 .> UC21 : <<extend>>

UC24 ..> UC23 : <<extend>>
UC26 ..> UC23 : <<extend>>
UC23 -- INS
UC23 -- EMP
UC26 -- EMP
UC26 -- LIB
@enduml
```

</div>

---

## UCD-04: حزمة الجدولة (Scheduling)

**الحالات:** UC-27 … UC-33. **الفاعلون:** INS، وCRD، وHOD، وDEN، وACO، وSTU. **يوضّح المخطط:** التفرّغ ومتابعته، وتوليد الجدول وإرساله للاعتماد ونشره، وعرض الجدول الأسبوعي، وطلبات الاعتذار والتعويض.

**العلاقات:**

- توسّع «تقديم طلب اعتذار أو تعويض عن محاضرة» UC-33 حالة «عرض الجدول الأسبوعي» UC-32، لأن المدرّس يبدؤها من محاضرة في جدوله.

![UCD-04-scheduling: حزمة الجدولة (Scheduling)](Images/UCD-04-scheduling.png)

<div dir="ltr">

```plantuml
@startuml UCD-04-scheduling
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "رئيس القسم\nHOD" as HOD
actor "عميد الكلية\nDEN" as DEN
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "عضو هيئة التدريس\nINS" as INS
actor "الطالب\nSTU" as STU

package "الجدولة\nScheduling" {
  usecase "إدخال أوقات التفرّغ\nUC-27" as UC27
  usecase "متابعة أوقات تفرّغ\nالمدرّسين وتذكيرهم\nUC-28" as UC28
  usecase "توليد الجدول الدراسي\nUC-29" as UC29
  usecase "إرسال الجدول للاعتماد\nUC-30" as UC30
  usecase "اعتماد الجدول ونشره\nUC-31" as UC31
  usecase "تقديم طلب اعتذار\nأو تعويض عن محاضرة\nUC-33" as UC33
  usecase "عرض الجدول الأسبوعي\nUC-32" as UC32
}

HOD -- UC28
DEN -- UC28
CRD -- UC28
CRD -- UC29
CRD -- UC30
ACO -- UC31

UC27 -- INS
UC33 -- INS
UC32 -- INS
UC32 -- STU
UC33 .> UC32 : <<extend>>
@enduml
```

</div>

---

## UCD-05: حزمة الامتحانات والدرجات (Exams and Grades)

**الحالات:** UC-34 … UC-35. **الفاعلون:** EXM، وSTU. **يوضّح المخطط:** رصد علامات الامتحان وعرض الدرجات.

![UCD-05-grades: حزمة الامتحانات والدرجات (Exams and Grades)](Images/UCD-05-grades.png)

<div dir="ltr">

```plantuml
@startuml UCD-05-grades
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "موظف شؤون\nالامتحانات\nEXM" as EXM
actor "الطالب\nSTU" as STU

package "الامتحانات والدرجات\nExams and Grades" {
  usecase "رصد علامات الامتحان\nUC-34" as UC34
  usecase "عرض الدرجات\nUC-35" as UC35
}

EXM -- UC34
UC35 -- STU
@enduml
```

</div>

---

## UCD-06: حزمة التقويم والتقارير والنظام (Calendar, Reports and System)

**الحالات:** UC-36 … UC-38. **الفاعلون:** ACO، وEXE، وADM. **يوضّح المخطط:** نقل الفصل الدراسي بين مراحله، وتقارير الإدارة، والنسخ الاحتياطي والاستعادة.

![UCD-06-system: حزمة التقويم والتقارير والنظام (Calendar, Reports and System)](Images/UCD-06-system.png)

<div dir="ltr">

```plantuml
@startuml UCD-06-system
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "الإدارة العليا\nEXE" as EXE
actor "مدير النظام\nADM" as ADM

package "التقويم والتقارير والنظام\nCalendar, Reports and System" {
  usecase "نقل الفصل الدراسي\nبين مراحله\nUC-36" as UC36
  usecase "عرض تقارير الإدارة\nUC-37" as UC37
  usecase "إنشاء نسخة احتياطية\nواستعادتها\nUC-38" as UC38
}

ACO -- UC36
EXE -- UC37
ADM -- UC38
@enduml
```

</div>

---

## UCD-07: حزمة الإدارة والمتابعة (Administration and Monitoring)

**الحالات:** UC-39 … UC-47. **الفاعلون:** ADM، والمستخدم (أي دور)، وCRD، وACO، ونظام خارجي، وخدمة الإشعارات الفورية. **يوضّح المخطط:** الدخول باسم مستخدم آخر، وسجل التدقيق، وإعدادات النظام ووضع الصيانة، وصحة النظام، والاستيراد، والتكاملات ومفاتيحها؛ ثم البحث الشامل والإشعارات ولوحة التحكم المتاحة لكل دور.

**العلاقات:**

- يستورد CRD وACO البيانات من ملف في UC-43 بحسب صلاحياتهما، كما يستوردها ADM.
- يتصل النظام الخارجي بمفتاح يصدره ADM في UC-44، وتوصل خدمة الإشعارات الفورية إشعارات UC-46 إلى أجهزة المستخدمين.

![UCD-07-admin: حزمة الإدارة والمتابعة (Administration and Monitoring)](Images/UCD-07-admin.png)

<div dir="ltr">

```plantuml
@startuml UCD-07-admin
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "مدير النظام\nADM" as ADM
actor "المستخدم\nAny User" as USER

actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "نظام خارجي\nExternal System" as EXT
actor "خدمة الإشعارات\nالفورية\nFCM" as FCM

package "الإدارة والمتابعة\nAdministration and Monitoring" {
  usecase "الدخول باسم مستخدم آخر\nUC-39" as UC39
  usecase "استعراض سجل التدقيق\nUC-40" as UC40
  usecase "ضبط إعدادات النظام\nووضع الصيانة\nUC-41" as UC41
  usecase "مراقبة صحة النظام\nUC-42" as UC42
  usecase "استيراد البيانات من ملف\nUC-43" as UC43
  usecase "إدارة التكاملات ومفاتيح\nالواجهة البرمجية\nUC-44" as UC44
  usecase "البحث الشامل\nUC-45" as UC45
  usecase "متابعة الإشعارات\nUC-46" as UC46
  usecase "عرض لوحة التحكم\nUC-47" as UC47
}

note left of USER
  كل دور يرث
  هذه الحالات
end note

ADM -- UC39
ADM -- UC40
ADM -- UC41
ADM -- UC42
ADM -- UC43
ADM -- UC44
USER -- UC45
USER -- UC46
USER -- UC47

UC43 -- CRD
UC43 -- ACO
UC44 -- EXT
UC46 -- FCM
@enduml
```

</div>

---

## UCD-08: حزمة الهيكل الأكاديمي والخطط (Academic Structure and Plans)

**الحالات:** UC-48 … UC-56. **الفاعلون:** ADM، وDEN، وACO، وCRD. **يوضّح المخطط:** الفروع والمباني، والكليات والأقسام وقياداتها، والوحدات الإدارية، والبرامج، والنوافذ الزمنية والعطل وأدوار التسجيل، والمقررات ومتطلباتها، وسلالم الدرجات، والخطط الدراسية.

**العلاقات:**

- توسّع «تحديد المتطلبات السابقة والمعادلات» UC-54 حالة «إدارة المقررات وتوصيفها» UC-53.
- يشارك DEN في UC-49، ويشارك CRD في المقررات ومتطلباتها UC-53 وUC-54.

![UCD-08-structure: حزمة الهيكل الأكاديمي والخطط (Academic Structure and Plans)](Images/UCD-08-structure.png)

<div dir="ltr">

```plantuml
@startuml UCD-08-structure
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "مدير النظام\nADM" as ADM
actor "عميد الكلية\nDEN" as DEN

actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "منسق الجداول\nوالموارد\nCRD" as CRD

package "الهيكل الأكاديمي والخطط\nAcademic Structure and Plans" {
  usecase "إدارة الفروع والمباني\nUC-48" as UC48
  usecase "إدارة الكليات والأقسام\nوقياداتها\nUC-49" as UC49
  usecase "إدارة الوحدات الإدارية\nUC-51" as UC51
  usecase "إدارة البرامج الأكاديمية\nUC-50" as UC50
  usecase "إدارة النوافذ الزمنية والعطل\nوأدوار التسجيل\nUC-52" as UC52
  usecase "إدارة سلالم الدرجات\nUC-55" as UC55
  usecase "إعداد الخطة الدراسية\nواعتمادها\nUC-56" as UC56
  usecase "إدارة المقررات وتوصيفها\nUC-53" as UC53
  usecase "تحديد المتطلبات السابقة\nوالمعادلات\nUC-54" as UC54
}

ADM -- UC48
ADM -- UC49
ADM -- UC51
ADM -- UC50
DEN -- UC49

UC50 -- ACO
UC52 -- ACO
UC55 -- ACO
UC56 -- ACO
UC53 -- ACO
UC53 -- CRD
UC53 <. UC54 : <<extend>>
UC54 -- ACO
UC54 -- CRD
@enduml
```

</div>

---

## UCD-09: حزمة إعداد الجدولة وتشغيلها (Scheduling Preparation and Operations)

**الحالات:** UC-57 … UC-62. **الفاعلون:** CRD، وADM، وACO، وDEN، وHOD، وINS. **يوضّح المخطط:** الملف التدريسي لعضو هيئة التدريس، وطرح المقررات وتقدير الطلب، والشعب وإسناد مدرّسيها، وقواعد الجدولة وقيودها، ومعالجة التعارضات ومؤشر الجودة، والإعادة الطارئة للجدولة.

**العلاقات:**

- توسّع «معالجة تعارضات الجدول ومؤشر الجودة» UC-61 حالة «توليد الجدول الدراسي» UC-29 من حزمة الجدولة، فتظهر UC-29 بإطار رمادي متقطع.

![UCD-09-scheduling-ops: حزمة إعداد الجدولة وتشغيلها (Scheduling Preparation and Operations)](Images/UCD-09-scheduling-ops.png)

<div dir="ltr">

```plantuml
@startuml UCD-09-scheduling-ops
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "مدير النظام\nADM" as ADM

actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "عميد الكلية\nDEN" as DEN
actor "رئيس القسم\nHOD" as HOD
actor "عضو هيئة التدريس\nINS" as INS

package "إعداد الجدولة وتشغيلها\nScheduling Preparation and Operations" {
  usecase "معالجة تعارضات الجدول\nومؤشر الجودة\nUC-61" as UC61
  usecase "الإعادة الطارئة للجدولة\nواقتراح البدلاء\nUC-62" as UC62
  usecase "إنشاء الشعب\nوإسناد مدرّسيها\nUC-59" as UC59
  usecase "طرح المقررات\nوتقدير الطلب\nUC-58" as UC58
  usecase "ضبط قواعد الجدولة\nوقيودها\nUC-60" as UC60
  usecase "إدارة الملف التدريسي\nلعضو هيئة التدريس\nUC-57" as UC57
}

usecase "توليد الجدول الدراسي\nمن حزمة الجدولة\nUC-29" as UC29 #F5F5F5;line.dashed

ADM -- UC60
CRD -- UC60
CRD -- UC58
CRD -- UC59
CRD -- UC61
CRD -- UC62
UC61 ..> UC29 : <<extend>>

UC58 -- ACO
UC57 -- ACO
UC57 -- DEN
UC57 -- HOD
UC57 -- INS
@enduml
```

</div>

---

## UCD-10: حزمة سجلات الطلاب والتسجيل (Student Records and Registration)

**الحالات:** UC-63 … UC-71. **الفاعلون:** STU، وADM، وADO، وACO، وADV. **يوضّح المخطط:** سجلات الطلاب والتدقيق الأكاديمي والتخرج، ونشر كتالوج التسجيل، وتسجيل المقررات وأهليته وقوائم الانتظار والسحب والإضافة، واستثناءات التسجيل والعوائق.

**العلاقات:**

- تتضمن «تسجيل المقررات» UC-67 و«السحب والإضافة» UC-70 حالة «التحقق من أهلية التسجيل» UC-68.
- توسّع «الانضمام إلى قائمة الانتظار وقبول المقعد» UC-69 حالة «تسجيل المقررات» UC-67 عند امتلاء الشعبة.
- تتضمن «ترشيح المتخرجين واعتماد دفعة التخرج» UC-65 حالة «عرض التدقيق الأكاديمي» UC-64.

![UCD-10-registration: حزمة سجلات الطلاب والتسجيل (Student Records and Registration)](Images/UCD-10-registration.png)

<div dir="ltr">

```plantuml
@startuml UCD-10-registration
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "الطالب\nSTU" as STU
actor "مدير النظام\nADM" as ADM
actor "موظف القبول\nADO" as ADO

actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "المرشد الأكاديمي\nADV" as ADV

package "سجلات الطلاب والتسجيل\nStudent Records and Registration" {
  usecase "الانضمام إلى قائمة الانتظار\nوقبول المقعد\nUC-69" as UC69
  usecase "تسجيل المقررات\nUC-67" as UC67
  usecase "السحب والإضافة\nUC-70" as UC70
  usecase "عرض التدقيق الأكاديمي\nUC-64" as UC64
  usecase "إدارة سجلات الطلاب\nUC-63" as UC63
  usecase "التحقق من أهلية التسجيل\nUC-68" as UC68
  usecase "ترشيح المتخرجين\nواعتماد دفعة التخرج\nUC-65" as UC65
  usecase "نشر كتالوج التسجيل\nوفتح أدواره\nUC-66" as UC66
  usecase "منح استثناءات التسجيل\nوإدارة العوائق\nUC-71" as UC71
}

STU -- UC67
STU -- UC70
STU -- UC64
ADM -- UC63
ADO -- UC63
UC67 <. UC69 : <<extend>>
UC67 ..> UC68 : <<include>>
UC70 ..> UC68 : <<include>>
UC64 <.. UC65 : <<include>>

UC66 -- ACO
UC71 -- ACO
UC65 -- ACO
UC64 --- ACO
UC64 --- ADV
@enduml
```

</div>

---

## UCD-11: حزمة الحضور والتعلّم والتقييم (Attendance, Learning and Evaluation)

**الحالات:** UC-72 … UC-77. **الفاعلون:** INS، وSTU، وACO، وHOD، وDEN. **يوضّح المخطط:** تسجيل حضور الجلسة ومتابعة الغياب واعتماد الحرمان، ومحتوى المادة وإعلاناتها، وإنشاء الكويزات وأداؤها، وتقييم المقرر والمدرّس.

![UCD-11-learning: حزمة الحضور والتعلّم والتقييم (Attendance, Learning and Evaluation)](Images/UCD-11-learning.png)

<div dir="ltr">

```plantuml
@startuml UCD-11-learning
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "عضو هيئة التدريس\nINS" as INS
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO

actor "الطالب\nSTU" as STU
actor "رئيس القسم\nHOD" as HOD
actor "عميد الكلية\nDEN" as DEN

package "الحضور والتعلّم والتقييم\nAttendance, Learning and Evaluation" {
  usecase "إنشاء كويز ونشره\nUC-75" as UC75
  usecase "تسجيل حضور الجلسة\nUC-72" as UC72
  usecase "إدارة محتوى المادة\nوإعلاناتها\nUC-74" as UC74
  usecase "متابعة الغياب\nواعتماد الحرمان\nUC-73" as UC73
  usecase "أداء الكويز\nUC-76" as UC76
  usecase "تقييم المقرر والمدرّس\nUC-77" as UC77
}

INS -- UC75
INS -- UC72
INS -- UC74
INS -- UC77
ACO -- UC73

UC72 -- STU
UC74 -- STU
UC73 -- STU
UC76 -- STU
UC77 -- STU
UC77 -- HOD
UC77 -- DEN
@enduml
```

</div>

---

## UCD-12: حزمة سير اعتماد الدرجات (Grade Approval Workflow)

**الحالات:** UC-78 … UC-83. **الفاعلون:** INS، وHOD، وEXM، وDEN، وSTU، وACO. **يوضّح المخطط:** رصد كشف الدرجات ومراجعته في القسم، والإدخال المزدوج واعتماد الكشوف ونشرها، وحساب المعدل والوضع الأكاديمي، وإصدار كشف الدرجات، وطلب تعديل درجة منشورة.

**العلاقات:**

- تتضمن «الإدخال المزدوج واعتماد الكشوف ونشرها» UC-80 و«طلب تعديل درجة منشورة» UC-83 حالة «حساب المعدل والوضع الأكاديمي» UC-81.

![UCD-12-grades-workflow: حزمة سير اعتماد الدرجات (Grade Approval Workflow)](Images/UCD-12-grades-workflow.png)

<div dir="ltr">

```plantuml
@startuml UCD-12-grades-workflow
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "عضو هيئة التدريس\nINS" as INS
actor "رئيس القسم\nHOD" as HOD

actor "موظف شؤون\nالامتحانات\nEXM" as EXM
actor "عميد الكلية\nDEN" as DEN
actor "الطالب\nSTU" as STU
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO

package "سير اعتماد الدرجات\nGrade Approval Workflow" {
  usecase "رصد كشف الدرجات\nوإرساله للمراجعة\nUC-78" as UC78
  usecase "مراجعة كشف الدرجات\nفي القسم\nUC-79" as UC79
  usecase "الإدخال المزدوج واعتماد\nالكشوف ونشرها\nUC-80" as UC80
  usecase "طلب تعديل درجة منشورة\nUC-83" as UC83
  usecase "حساب المعدل\nوالوضع الأكاديمي\nUC-81" as UC81
  usecase "إصدار كشف الدرجات\nUC-82" as UC82
}

INS -- UC78
HOD -- UC79
INS -- UC83
UC80 ..> UC81 : <<include>>
UC83 ..> UC81 : <<include>>

UC80 --- EXM
UC83 --- DEN
UC82 -- STU
UC82 -- ACO
@enduml
```

</div>

---

## UCD-13: حزمة جدولة الامتحانات وتنفيذها (Exam Scheduling and Operations)

**الحالات:** UC-84 … UC-87. **الفاعلون:** EXM، وINS (مراقباً)، وSTU. **يوضّح المخطط:** جدولة الامتحانات، وتوزيع القاعات والمقاعد والمراقبين، وجدول امتحانات الطالب وبطاقته، وإدارة يوم الامتحان.

![UCD-13-exams: حزمة جدولة الامتحانات وتنفيذها (Exam Scheduling and Operations)](Images/UCD-13-exams.png)

<div dir="ltr">

```plantuml
@startuml UCD-13-exams
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "موظف شؤون\nالامتحانات\nEXM" as EXM

actor "عضو هيئة التدريس\nمراقباً\nINS" as INS
actor "الطالب\nSTU" as STU

package "جدولة الامتحانات وتنفيذها\nExam Scheduling and Operations" {
  usecase "جدولة الامتحانات\nUC-84" as UC84
  usecase "توزيع القاعات والمقاعد\nوالمراقبين\nUC-85" as UC85
  usecase "إدارة يوم الامتحان\nUC-87" as UC87
  usecase "عرض جدول امتحاناتي\nوبطاقة الامتحان\nUC-86" as UC86
}

EXM -- UC84
EXM -- UC85
EXM -- UC87

UC85 -- INS
UC87 -- INS
UC86 -- STU
@enduml
```

</div>

---

## UCD-14: حزمة القبول والإرشاد (Admission and Advising)

**الحالات:** UC-88 … UC-92. **الفاعلون:** ADO، وAPL، وبوابة الدفع الإلكتروني، وADV، وSTU. **يوضّح المخطط:** دورات القبول، وتقديم طلبات القبول ومتابعتها، والمفاضلة وقرارات القبول، ومراجعة الخطة الفصلية ومنح تصريح التسجيل، والإنذارات ومواعيد الإرشاد.

**العلاقات:**

- تشارك بوابة الدفع الإلكتروني في «تقديم طلب القبول ومتابعته» UC-89 لدفع رسوم الطلب.

![UCD-14-admission-advising: حزمة القبول والإرشاد (Admission and Advising)](Images/UCD-14-admission-advising.png)

<div dir="ltr">

```plantuml
@startuml UCD-14-admission-advising
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "موظف القبول\nADO" as ADO
actor "المتقدّم\nAPL" as APL

actor "بوابة الدفع\nالإلكتروني\nPayment Gateway" as PG
actor "المرشد الأكاديمي\nADV" as ADV
actor "الطالب\nSTU" as STU

package "القبول والإرشاد\nAdmission and Advising" {
  usecase "إدارة دورات القبول\nUC-88" as UC88
  usecase "المفاضلة وإصدار\nقرارات القبول\nUC-90" as UC90
  usecase "تقديم طلب القبول\nومتابعته\nUC-89" as UC89
  usecase "مراجعة الخطة الفصلية\nومنح تصريح التسجيل\nUC-91" as UC91
  usecase "متابعة الإنذارات\nومواعيد الإرشاد\nUC-92" as UC92
}

ADO -- UC88
ADO -- UC90
ADO -- UC89
APL -- UC89

UC89 -- PG
UC91 -- ADV
UC92 -- ADV
UC91 -- STU
UC92 -- STU
@enduml
```

</div>

---

## UCD-15: حزمة المالية (Finance)

**الحالات:** UC-93 … UC-96. **الفاعلون:** FIN، وSTU، وبوابة الدفع الإلكتروني. **يوضّح المخطط:** الرسوم والفواتير، والرصيد والدفع الإلكتروني، وتسجيل الدفعات في الصندوق، والأقساط والمنح والغرامات والاسترداد.

**العلاقات:**

- تشارك بوابة الدفع الإلكتروني في «عرض الرصيد والدفع الإلكتروني» UC-94، ويقدّم الطالب طلب التقسيط الذي يعالجه FIN في UC-96.

![UCD-15-finance: حزمة المالية (Finance)](Images/UCD-15-finance.png)

<div dir="ltr">

```plantuml
@startuml UCD-15-finance
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "الموظف المالي\nFIN" as FIN

actor "الطالب\nSTU" as STU
actor "بوابة الدفع\nالإلكتروني\nPayment Gateway" as PG

package "المالية\nFinance" {
  usecase "إدارة الرسوم والفواتير\nUC-93" as UC93
  usecase "تسجيل دفعة في الصندوق\nUC-95" as UC95
  usecase "إدارة الأقساط والمنح\nوالاسترداد\nUC-96" as UC96
  usecase "عرض الرصيد\nوالدفع الإلكتروني\nUC-94" as UC94
}

FIN -- UC93
FIN -- UC95
FIN -- UC96

UC96 -- STU
UC94 -- STU
UC94 -- PG
@enduml
```

</div>

---

## UCD-16: حزمة المكتبة وشؤون الموظفين والطلبات (Library, Staff Affairs and E-Requests)

**الحالات:** UC-97 … UC-103. **الفاعلون:** STU، وINS، وLIB، وHRO، وEMP، وجهاز البصمة، والمدير المباشر، وACO، وEXM. **يوضّح المخطط:** البحث في كتالوج المكتبة والحجز والإعارة، وملفات الموظفين وعقودهم ودوامهم، وطلبات الإجازة واعتمادها، والطلبات الإلكترونية تقديماً ومعالجة.

**العلاقات:**

- توسّع «الإعادة الطارئة للجدولة واقتراح البدلاء» UC-62 من حزمة إعداد الجدولة حالة «اعتماد طلبات الإجازة» UC-101، حين تكون الإجازة لعضو هيئة تدريس له محاضرات في مدتها.
- يرسل جهاز البصمة الدوام في UC-99 بمفتاح يصدره ADM في UC-44.

![UCD-16-services: حزمة المكتبة وشؤون الموظفين والطلبات (Library, Staff Affairs and E-Requests)](Images/UCD-16-services.png)

<div dir="ltr">

```plantuml
@startuml UCD-16-services
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "موظف شؤون\nالامتحانات\nEXM" as EXM
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO
actor "أمين المكتبة\nLIB" as LIB
actor "جهاز البصمة" as BIO
actor "موظف شؤون\nالموظفين\nHRO" as HRO
actor "المدير المباشر" as MGR

actor "الطالب\nSTU" as STU
actor "عضو هيئة التدريس\nINS" as INS
actor "موظف\nEMP" as EMP

package "المكتبة وشؤون الموظفين والطلبات\nLibrary, Staff Affairs and E-Requests" {
  usecase "تقديم طلب إلكتروني\nومتابعته\nUC-102" as UC102
  usecase "معالجة الطلبات\nالإلكترونية\nUC-103" as UC103
  usecase "البحث في كتالوج المكتبة\nوحجز نسخة\nUC-97" as UC97
  usecase "إعارة النسخ وإرجاعها\nUC-98" as UC98
  usecase "تقديم طلب إجازة\nUC-100" as UC100
  usecase "إدارة ملفات الموظفين\nوعقودهم\nUC-99" as UC99
  usecase "اعتماد طلبات الإجازة\nUC-101" as UC101
}

usecase "الإعادة الطارئة للجدولة\nواقتراح البدلاء\nمن حزمة إعداد الجدولة\nUC-62" as UC62 #F5F5F5;line.dashed

EXM -- UC103
ACO -- UC103
LIB -- UC98
BIO -- UC99
HRO -- UC99
HRO -- UC101
MGR -- UC101

UC102 -- STU
UC103 -- STU
UC97 -- STU
UC97 -- INS
UC100 -- INS
UC100 -- EMP
UC99 -- EMP
UC101 <.. UC62 : <<extend>>
@enduml
```

</div>

---

## UCD-17: حزمة الذكاء الاصطناعي والتحليلات (AI and Analytics)

**الحالات:** UC-104 … UC-113. **الفاعلون:** ADM، وEXE، وCRD، وINS، والمستخدم (أي دور)، وACO، وADV، وHOD، ومزوّد النماذج اللغوية. **يوضّح المخطط:** بوابة الذكاء الاصطناعي ومتابعة استخدامها، والمساعد الذكي وقاعدة معرفة اللوائح، والإدخال بلغة طبيعية وشرح نتيجة الجدولة، والتنبؤ بالطلب ومؤشر خطر التعثّر، واستخراج المقررات من ملف وملخصات التقارير، ومحاكاة السيناريوهات.

**العلاقات:**

- يشارك مزوّد النماذج اللغوية في الحالات التي تولّد نصاً أو تضمينات، عبر البوابة التي يضبطها ADM في UC-104؛ أما التنبؤ UC-109 ومؤشر الخطر UC-110 والمحاكاة UC-113 فلا تحتاج إليه.
- تُكمل حالات هذه الحزمة شاشات قائمة ولا تحل محلها: UC-107 إدخالَ التفرّغ UC-27 وقيودَ الجدولة UC-60، وUC-108 نتيجةَ التوليد UC-29، وUC-109 تقديرَ الطلب UC-58، وUC-111 استيرادَ المقررات UC-43، وUC-112 لوحةَ التحكم UC-47 وتقاريرَ الإدارة UC-37.

![UCD-17-ai: حزمة الذكاء الاصطناعي والتحليلات (AI and Analytics)](Images/UCD-17-ai.png)

<div dir="ltr">

```plantuml
@startuml UCD-17-ai
' ===== النمط الموحّد (انسخه مع المخطط) =====
skinparam dpi 150
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 12
skinparam defaultTextAlignment center
skinparam ArrowColor #455A64
skinparam ArrowFontSize 12
skinparam ArrowFontColor #37474F
skinparam actor {
  BorderColor #37474F
  BackgroundColor #ECEFF1
  FontSize 14
  FontStyle bold
}
skinparam usecase {
  BackgroundColor #E3F2FD
  BorderColor #1E88E5
  FontSize 14
}
skinparam package {
  BackgroundColor #FCFCFC
  BorderColor #78909C
  FontSize 16
  FontStyle bold
}
left to right direction
' ===== المخطط =====

actor "مدير النظام\nADM" as ADM
actor "الإدارة العليا\nEXE" as EXE
actor "منسق الجداول\nوالموارد\nCRD" as CRD
actor "عضو هيئة التدريس\nINS" as INS
actor "المستخدم\nAny User" as USER
actor "موظف الشؤون\nالأكاديمية\nACO" as ACO

actor "مزوّد النماذج\nاللغوية\nLLM Provider" as LLM
actor "المرشد الأكاديمي\nADV" as ADV
actor "رئيس القسم\nHOD" as HOD

package "الذكاء الاصطناعي والتحليلات\nAI and Analytics" {
  usecase "ضبط بوابة الذكاء الاصطناعي\nومتابعة استخدامها\nUC-104" as UC104
  usecase "توليد ملخص\nلتقرير أو لوحة\nUC-112" as UC112
  usecase "محاكاة السيناريوهات\nUC-113" as UC113
  usecase "التنبؤ بالطلب\nعلى المقررات\nUC-109" as UC109
  usecase "شرح نتيجة الجدولة\nUC-108" as UC108
  usecase "إدخال التفرّغ والقيود\nبلغة طبيعية\nUC-107" as UC107
  usecase "محادثة المساعد الذكي\nUC-105" as UC105
  usecase "إدارة قاعدة\nمعرفة اللوائح\nUC-106" as UC106
  usecase "استخراج بيانات المقررات\nمن ملف\nUC-111" as UC111
  usecase "متابعة مؤشر\nخطر التعثّر\nUC-110" as UC110
}

ADM -- UC104
ADM -- UC112
EXE -- UC104
EXE -- UC112
EXE -- UC113
EXE -- UC109
CRD -- UC113
CRD -- UC109
CRD -- UC108
CRD -- UC107
INS -- UC108
INS -- UC107
USER -- UC105
ACO -- UC109
ACO -- UC106
ACO -- UC111
ACO -- UC110

UC104 -- LLM
UC112 -- LLM
UC108 -- LLM
UC107 -- LLM
UC105 -- LLM
UC106 -- LLM
UC111 -- LLM
UC110 -- ADV
UC110 -- HOD
@enduml
```

</div>

---

## ملاحظات

- اتجاه سهم «include» من الحالة التي تتضمن إلى الحالة المتضمَّنة، واتجاه سهم «extend» من الحالة الموسِّعة إلى الحالة الأساسية. لذلك يتجه السهم في مخطط الموارد من «إدارة القاعات» إلى «تحديد سعة الامتحان»، ومن «طلب موارد إضافية» إلى «عرض الموارد»، كما تنص السيناريوهات.
- الحالات الجامعة («إدارة الملف الشخصي» و«إدارة المستخدمين» و«إدارة الأدوار») مأخوذة من مخططات الفريق الأولى، وليس لها سيناريو مستقل لأن سيناريوهات الحالات المتفرعة منها تغطيها.
- يربط المخطط العام كل حزمة بفاعليها الرئيسيين فقط حتى يبقى مقروءاً، أما ارتباط كل فاعل بكل حالة فكامل في مخطط الحزمة.
- عند تغيير سيناريو أو إضافة حالة، يُعدَّل ملف `Src` المناسب وتُولَّد صورته من جديد، ثم تُحدَّث الكتلة نفسها في هذه الوثيقة.

</div>
