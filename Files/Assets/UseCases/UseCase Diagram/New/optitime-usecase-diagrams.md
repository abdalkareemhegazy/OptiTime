<div dir="rtl">

> **الوثيقة:** مخططات حالات الاستخدام (Use Case Diagrams) — **النظام:** OptiTime — **التاريخ:** 2026-11-08

# مخططات حالات الاستخدام — نظام OptiTime

تضم هذه الوثيقة ثلاثة عشر مخطط حالات استخدام تغطي وحدات النظام الثلاث والعشرين وحالات الاستخدام المئة والثلاث عشرة في وثيقة السيناريوهات. وصيغت أسماء الحالات والفاعلين بكلمات بسيطة يفهمها أي قارئ، وجُمعت عمليات الإضافة والتعديل والحذف والعرض في حالة «إدارة …» واحدة، ووُزّعت الأدوار بحسب سيناريوهات حالات الاستخدام ومصفوفة الصلاحيات (RACI) في المقترح.

**الملفات:** كود كل مخطط في مجلد `Src` وصورته في مجلد `Images` بالاسم نفسه، والكود في هذه الوثيقة مطابق حرفياً لملفات `Src`.

## قواعد الرسم

| العنصر | معناه |
|---|---|
| فاعل على اليسار | شخص يستخدم النظام |
| فاعل على اليمين | خدمة أو جهاز أو نظام خارجي يتعامل معه النظام |
| خط متصل | الفاعل ينفّذ الحالة، أو يتخذ فيها قراراً، أو يطّلع بها على ما يخصه |
| سهم متقطع «include» | يتجه من الحالة الأساسية إلى الحالة المتضمَّنة، وتُنفَّذ المتضمَّنة في كل مرة |
| سهم متقطع «extend» | يتجه من الحالة الموسِّعة إلى الحالة الأساسية، وتُنفَّذ الموسِّعة عند شرط أو اختيار فقط |
| سهم برأس مثلث فارغ | تعميم: الفاعل الفرعي نوع من الفاعل العام ويرث حالاته |
| إطار بعنوان | حدود النظام في المجال الذي يغطيه المخطط |

## الفاعلون

| الفاعل | من هو |
|---|---|
| المستخدم (أي دور) | كل من له حساب في النظام، وكل دور يرث حالاته. |
| مدير النظام | يدير الحسابات والصلاحيات والإعدادات والهيكل التنظيمي والنسخ الاحتياطي. |
| الإدارة العليا | رئاسة الجامعة: تطّلع على التقارير وتجرّب الاحتمالات المستقبلية. |
| عميد الكلية | يدير أقسام كليته ويتابع مدرّسيها ويعتمد التعديل الكبير للعلامات. |
| رئيس القسم | يراجع علامات شعب قسمه ويتابع مدرّسيه. |
| منسق الجداول والموارد | يطرح المقررات وينشئ الشعب ويبني الجدول ويدير القاعات والأجهزة. |
| موظف الشؤون الأكاديمية | يعتمد الطرح والجدول وتعديل العلامات الصغير، ويدير التقويم والخطط والتسجيل والتخرج. |
| موظف شؤون الامتحانات | يجدول الامتحانات ويطابق العلامات وينشرها. |
| موظف القبول | يدير دورات القبول والمفاضلة وملفات الطلاب. |
| المرشد الأكاديمي | يراجع خطط طلابه ويمنحهم إذن التسجيل ويتابع تعثّرهم. |
| عضو هيئة التدريس | يحدد تفرّغه ويدرّس ويسجّل الحضور ويدخل العلامات. |
| الطالب | يسجّل مقرراته ويتابع جدوله وعلاماته ورسومه وطلباته. |
| المتقدّم للقبول | يقدّم طلب الالتحاق قبل أن يصبح طالباً. |
| الموظف المالي | يدير الرسوم والفواتير والصندوق والأقساط والمنح. |
| موظف شؤون الموظفين | يدير ملفات الموظفين وعقودهم ويعتمد إجازاتهم. |
| أمين المكتبة | يعير الكتب ويستلمها. |
| الموظف | أي عامل في الجامعة: يطّلع على ملفه ودوامه ويطلب الإجازة ويحجز القاعات. |
| المدير المباشر | مسؤول الموظف الذي يوافق أولاً على إجازته. |
| خدمة البريد الإلكتروني | ترسل رمز استعادة كلمة المرور. |
| خدمة إشعارات الجوال | توصل الإشعارات الفورية إلى أجهزة المستخدمين. |
| مزوّد الذكاء الاصطناعي | النموذج اللغوي الذي يفهم النصوص ويكتب الإجابات والملخصات. |
| بوابة الدفع الإلكتروني | تنفّذ دفع رسوم التقديم والفواتير. |
| نظام خارجي | نظام آخر يتصل بالنظام بمفتاح يصدره مدير النظام. |
| جهاز البصمة | يرسل حضور الموظفين وانصرافهم. |

## تغطية وحدات النظام

| الوحدة | المخطط |
|---|---|
| الهوية والدخول | 01، 02 |
| إدارة النظام | 02 |
| التواصل والإشعارات | 01 |
| الهيكل التنظيمي | 03 |
| التقويم الأكاديمي | 03 |
| الخطط والمقررات | 04 |
| الموارد | 05 |
| الجدولة | 06 |
| سجلات الطلاب | 09، 10 |
| تسجيل المقررات | 09 |
| الحضور | 07 |
| التعلّم | 07 |
| الدرجات | 08، 10 |
| الامتحانات | 08 |
| القبول | 09 |
| الإرشاد الأكاديمي | 10 |
| المالية | 11 |
| المكتبة | 12 |
| شؤون الموظفين | 12 |
| الطلبات الإلكترونية | 11 |
| تقييم المقررات | 07 |
| التقارير والتحليلات | 13 |
| الذكاء الاصطناعي | 01، 10، 13 |

## فهرس المخططات

| الرقم | المخطط | الحالات | الفاعلون |
|---|---|---|---|
| 01 | حسابي والخدمات المشتركة | 12 | المستخدم (أي دور)، وخدمة البريد الإلكتروني، وخدمة إشعارات الجوال، ومزوّد الذكاء الاصطناعي |
| 02 | إدارة النظام | 7 | مدير النظام، وموظف الشؤون الأكاديمية، ومنسق الجداول والموارد، ونظام خارجي |
| 03 | الهيكل التنظيمي والتقويم الأكاديمي | 8 | مدير النظام، وعميد الكلية، وموظف الشؤون الأكاديمية، والمستخدم (أي دور) |
| 04 | المقررات والخطط الدراسية | 6 | موظف الشؤون الأكاديمية، ومنسق الجداول والموارد، ومدير النظام، ورئيس القسم، وعميد الكلية، وعضو هيئة التدريس |
| 05 | القاعات والموارد | 8 | منسق الجداول والموارد، ومدير النظام، والموظف، وأمين المكتبة، وعضو هيئة التدريس |
| 06 | الجدول الدراسي | 14 | منسق الجداول والموارد، وموظف الشؤون الأكاديمية، ومدير النظام، ورئيس القسم، وعميد الكلية، وعضو هيئة التدريس، والطالب |
| 07 | التدريس والحضور | 9 | عضو هيئة التدريس، والطالب، وموظف الشؤون الأكاديمية، ورئيس القسم، وعميد الكلية |
| 08 | الامتحانات والعلامات | 11 | موظف شؤون الامتحانات، وعضو هيئة التدريس، وموظف الشؤون الأكاديمية، ورئيس القسم، وعميد الكلية، والطالب |
| 09 | القبول والتسجيل | 13 | موظف القبول، والمتقدّم للقبول، وموظف الشؤون الأكاديمية، والطالب، وبوابة الدفع الإلكتروني |
| 10 | سجلات الطلاب والإرشاد | 11 | موظف القبول، ومدير النظام، وموظف الشؤون الأكاديمية، والطالب، والمرشد الأكاديمي |
| 11 | المالية والطلبات الإلكترونية | 7 | الموظف المالي، والطالب، والمرشد الأكاديمي، وموظف الشؤون الأكاديمية، وموظف شؤون الامتحانات، وبوابة الدفع الإلكتروني |
| 12 | المكتبة وشؤون الموظفين | 9 | الطالب، والموظف، وعضو هيئة التدريس، وأمين المكتبة، والمدير المباشر، وموظف شؤون الموظفين، وجهاز البصمة |
| 13 | التقارير والذكاء الاصطناعي | 10 | موظف الشؤون الأكاديمية، ومدير النظام، والإدارة العليا، ومنسق الجداول والموارد، وعضو هيئة التدريس، ومزوّد الذكاء الاصطناعي |

---

## 01. حسابي والخدمات المشتركة (My Account and Shared Services)

**الفاعلون:** المستخدم (أي دور)، وخدمة البريد الإلكتروني، وخدمة إشعارات الجوال، ومزوّد الذكاء الاصطناعي. **يوضّح المخطط:** ما يفعله كل مستخدم أياً كان دوره: الدخول والخروج، واستعادة كلمة المرور، والملف الشخصي، ولوحة التحكم، والبحث، والإشعارات، وسؤال المساعد الذكي.

**العلاقات:**

- «إدخال رمز التحقق من تطبيق الجوال» توسّع «تسجيل الدخول» حين يكون التحقق بخطوتين مفعّلاً للحساب.
- «استعادة كلمة المرور المنسية» تتضمن دائماً «التحقق من الرمز المرسل إلى البريد» ثم «تغيير كلمة المرور».
- «تغيير كلمة المرور» و«تفعيل التحقق بخطوتين» توسّعان «إدارة الملف الشخصي» حين يختارهما المستخدم.
- ترسل خدمة البريد رمز الاستعادة، وتوصل خدمة إشعارات الجوال الإشعارات، ويكتب مزوّد الذكاء الاصطناعي إجابات المساعد.
- كل أدوار النظام ترث حالات «المستخدم (أي دور)».

![UCD-01-account: حسابي والخدمات المشتركة](Images/UCD-01-account.png)

<div dir="ltr">

```plantuml
@startuml UCD-01-account
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

actor "المستخدم\n(أي دور)" as USER
actor "خدمة البريد\nالإلكتروني" as MAIL
actor "خدمة إشعارات\nالجوال" as FCM
actor "مزوّد الذكاء\nالاصطناعي" as LLM

rectangle "حسابي والخدمات المشتركة\nMy Account and Shared Services" {
  usecase "تسجيل الدخول" as LOGIN
  usecase "استعادة كلمة المرور\nالمنسية" as RECOVER
  usecase "إدارة الملف الشخصي" as PROFILE
  usecase "تسجيل الخروج" as LOGOUT
  usecase "عرض لوحة التحكم" as DASH
  usecase "البحث في النظام" as SEARCH
  usecase "متابعة الإشعارات" as NOTIF
  usecase "سؤال المساعد الذكي" as AI
  usecase "إدخال رمز التحقق\nمن تطبيق الجوال" as CODE
  usecase "التحقق من الرمز\nالمرسل إلى البريد" as MAILCODE
  usecase "تغيير كلمة المرور" as CHPW
  usecase "تفعيل التحقق\nبخطوتين" as TWOSTEP
}

note left of USER
  كل أدوار النظام
  ترث حالات المستخدم
end note

USER -- LOGIN
USER -- RECOVER
USER -- PROFILE
USER -- LOGOUT
USER -- DASH
USER -- SEARCH
USER -- NOTIF
USER -- AI

LOGIN <.. CODE : <<extend>>
RECOVER ..> MAILCODE : <<include>>
RECOVER ..> CHPW : <<include>>
PROFILE <.. CHPW : <<extend>>
PROFILE <.. TWOSTEP : <<extend>>

MAILCODE -- MAIL
NOTIF --- FCM
AI --- LLM
@enduml
```

</div>

---

## 02. إدارة النظام (System Administration)

**الفاعلون:** مدير النظام، وموظف الشؤون الأكاديمية، ومنسق الجداول والموارد، ونظام خارجي. **يوضّح المخطط:** ما يتولاه مدير النظام: المستخدمون وأدوارهم، والإعدادات ووضع الصيانة، وحالة النظام وسجل العمليات، والنسخ الاحتياطي، وربط النظام بالخدمات الخارجية، واستيراد البيانات من ملفات Excel.

**العلاقات:**

- «الدخول باسم مستخدم آخر لفحص مشكلته» توسّع «إدارة المستخدمين والأدوار»، فيبدؤها المدير من حساب المستخدم عند الحاجة.
- يستورد مدير النظام وموظف الشؤون الأكاديمية ومنسق الجداول، كلٌّ ما يملك إنشاءه يدوياً فقط.
- يتصل النظام الخارجي بمفتاح يصدره مدير النظام في «ربط النظام بالخدمات والأنظمة الخارجية».

![UCD-02-administration: إدارة النظام](Images/UCD-02-administration.png)

<div dir="ltr">

```plantuml
@startuml UCD-02-administration
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

actor "مدير النظام" as ADM
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "منسق الجداول\nوالموارد" as CRD
actor "نظام خارجي" as EXT

rectangle "إدارة النظام\nSystem Administration" {
  usecase "إدارة المستخدمين\nوالأدوار" as USERS
  usecase "ضبط إعدادات النظام\nووضع الصيانة" as SETTINGS
  usecase "متابعة حالة النظام\nوسجل العمليات" as HEALTH
  usecase "النسخ الاحتياطي\nواستعادة البيانات" as BACKUP
  usecase "ربط النظام بالخدمات\nوالأنظمة الخارجية" as INTEG
  usecase "استيراد البيانات\nمن ملفات Excel" as IMPORT
  usecase "الدخول باسم مستخدم\nآخر لفحص مشكلته" as IMP
}

ADM -- USERS
ADM -- SETTINGS
ADM -- HEALTH
ADM -- BACKUP
ADM -- INTEG
ADM -- IMPORT
ACO -- IMPORT
CRD -- IMPORT

USERS <.. IMP : <<extend>>
INTEG --- EXT
@enduml
```

</div>

---

## 03. الهيكل التنظيمي والتقويم الأكاديمي (Organization and Academic Calendar)

**الفاعلون:** مدير النظام، وعميد الكلية، وموظف الشؤون الأكاديمية، والمستخدم (أي دور). **يوضّح المخطط:** بناء الجامعة (الفروع والمباني، والكليات والأقسام وقياداتها، والوحدات الإدارية، والبرامج الأكاديمية)، والتقويم الأكاديمي (الفصول ومواعيدها وعطلها ومراحلها)، وعرض التقويم لكل مستخدم.

**العلاقات:**

- يدير مدير النظام الكليات والأقسام كلها، ويدير العميد أقسام كليته ويعيّن رؤساءها.
- ينشئ مدير النظام البرامج الأكاديمية ويغلقها، ويعدّل موظف الشؤون الأكاديمية لوائحها.
- «نقل الفصل الدراسي إلى مرحلته التالية» يتضمن «التحقق من اكتمال شروط الانتقال»، فلا ينتقل الفصل قبل اكتمالها.
- يشارك مدير النظام موظفَ الشؤون الأكاديمية إدارة الفصول ونقلها بين مراحلها.

![UCD-03-organization-calendar: الهيكل التنظيمي والتقويم الأكاديمي](Images/UCD-03-organization-calendar.png)

<div dir="ltr">

```plantuml
@startuml UCD-03-organization-calendar
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

actor "عميد الكلية" as DEN
actor "مدير النظام" as ADM
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "المستخدم\n(أي دور)" as USER

rectangle "الهيكل التنظيمي والتقويم الأكاديمي\nOrganization and Academic Calendar" {
  usecase "إدارة الكليات والأقسام\nوتعيين قياداتها" as COLLEGE
  usecase "إدارة الفروع والمباني" as BRANCH
  usecase "إدارة الوحدات الإدارية\n(كالمالية والمكتبة)" as UNITS
  usecase "إدارة البرامج الأكاديمية\nولوائحها" as PROG
  usecase "إدارة الفصول الدراسية\nومواعيدها وعطلها" as TERMS
  usecase "نقل الفصل الدراسي\nإلى مرحلته التالية" as PHASE
  usecase "عرض التقويم الأكاديمي\nوالاشتراك به" as CALVIEW
  usecase "التحقق من اكتمال\nشروط الانتقال" as COND
}

DEN -- COLLEGE
ADM -- COLLEGE
ADM -- BRANCH
ADM -- UNITS
ADM -- PROG
ADM -- TERMS
ADM -- PHASE
ACO -- PROG
ACO -- TERMS
ACO -- PHASE
USER -- CALVIEW

PHASE ..> COND : <<include>>
@enduml
```

</div>

---

## 04. المقررات والخطط الدراسية (Courses and Study Plans)

**الفاعلون:** موظف الشؤون الأكاديمية، ومنسق الجداول والموارد، ومدير النظام، ورئيس القسم، وعميد الكلية، وعضو هيئة التدريس. **يوضّح المخطط:** المقررات ومتطلباتها، والخطط الدراسية، وسلالم التقدير، وملف كل مدرّس: المقررات التي يدرّسها وساعاته المكتبية ورغباته في التدريس.

**العلاقات:**

- «تحديد المتطلبات السابقة والمقررات المعادلة» توسّع «إدارة المقررات ووصف محتواها» حين يحدد المستخدم ما يلزم لأخذ المقرر، ويرفض النظام أي متطلبات تدور في حلقة.
- يعدّ موظف الشؤون الأكاديمية الخطة الدراسية ويعتمدها، ويشاركه مدير النظام إدارة سلالم التقدير.
- يعدّ موظف الشؤون الأكاديمية ملفات المدرّسين جميعاً، والعميد ورئيس القسم ملفات مدرّسي نطاقهما: الرتبة وحدود الساعات الأسبوعية والمقررات التي يدرّسها كل مدرّس. ويحدد عضو هيئة التدريس بنفسه ساعاته المكتبية ورغبته في تدريس كل مقرر.

![UCD-04-curriculum: المقررات والخطط الدراسية](Images/UCD-04-curriculum.png)

<div dir="ltr">

```plantuml
@startuml UCD-04-curriculum
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

actor "منسق الجداول\nوالموارد" as CRD
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "مدير النظام" as ADM
actor "رئيس القسم" as HOD
actor "عميد الكلية" as DEN
actor "عضو هيئة\nالتدريس" as INS

rectangle "المقررات والخطط الدراسية\nCourses and Study Plans" {
  usecase "إدارة المقررات\nووصف محتواها" as COURSES
  usecase "إعداد الخطط الدراسية\nواعتمادها" as PLANS
  usecase "إدارة سلالم التقدير\n(الحروف والنقاط)" as SCALES
  usecase "إعداد ملف المدرّس\nوالمقررات التي يدرّسها" as TPROF
  usecase "تحديد ساعاتي المكتبية\nورغباتي في التدريس" as MYPROF
  usecase "تحديد المتطلبات السابقة\nوالمقررات المعادلة" as PREREQ
}

CRD -- COURSES
ACO -- COURSES
ACO -- PLANS
ACO -- SCALES
ADM -- SCALES
ACO -- TPROF
HOD -- TPROF
DEN -- TPROF
INS -- MYPROF

COURSES <.. PREREQ : <<extend>>
@enduml
```

</div>

---

## 05. القاعات والموارد (Rooms and Resources)

**الفاعلون:** منسق الجداول والموارد، ومدير النظام، والموظف، وأمين المكتبة، وعضو هيئة التدريس. **يوضّح المخطط:** إدارة القاعات والمختبرات والأجهزة وأعطالها، والبحث عن قاعة شاغرة وحجزها، وطلب موارد إضافية لمحاضرة والرد على الطلبات والحجوزات.

**العلاقات:**

- أمين المكتبة وعضو هيئة التدريس نوعان من «الموظف» (تعميم)، فيرثان البحث عن قاعة شاغرة وحجزها.
- «إدارة القاعات والمختبرات» تتضمن «تحديد مقاعد الامتحان في القاعة».
- «الإبلاغ عن عطل ومتابعة إصلاحه» توسّع «إدارة القاعات والمختبرات» و«إدارة الأجهزة والتجهيزات» عند وقوع عطل.
- «حجز قاعة» توسّع «البحث عن قاعة شاغرة» حين يختار الموظف قاعة ليحجزها، ويؤكّد المنسق الحجز في القاعات غير المفتوحة للحجز ضمن «الرد على طلبات الموارد والحجوزات».
- يشارك مدير النظام المنسقَ إدارة القاعات والأجهزة.

![UCD-05-resources: القاعات والموارد](Images/UCD-05-resources.png)

<div dir="ltr">

```plantuml
@startuml UCD-05-resources
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

actor "مدير النظام" as ADM
actor "منسق الجداول\nوالموارد" as CRD
actor "أمين المكتبة" as LIB
actor "الموظف" as EMP
actor "عضو هيئة\nالتدريس" as INS

rectangle "القاعات والموارد\nRooms and Resources" {
  usecase "إدارة القاعات\nوالمختبرات" as ROOMS
  usecase "إدارة الأجهزة\nوالتجهيزات" as EQUIP
  usecase "الرد على طلبات\nالموارد والحجوزات" as REQS
  usecase "البحث عن\nقاعة شاغرة" as FIND
  usecase "طلب قاعة أو تجهيزات\nإضافية لمحاضرة" as REQ
  usecase "تحديد مقاعد الامتحان\nفي القاعة" as CAP
  usecase "الإبلاغ عن عطل\nومتابعة إصلاحه" as MAINT
  usecase "حجز قاعة" as BOOK
}

LIB -|> EMP
EMP <|- INS

ADM -- ROOMS
ADM -- EQUIP
CRD -- ROOMS
CRD -- EQUIP
CRD -- REQS
EMP -- FIND
INS -- REQ

ROOMS ..> CAP : <<include>>
ROOMS <.. MAINT : <<extend>>
EQUIP <.. MAINT : <<extend>>
FIND <.. BOOK : <<extend>>
@enduml
```

</div>

---

## 06. الجدول الدراسي (Course Timetabling)

**الفاعلون:** منسق الجداول والموارد، وموظف الشؤون الأكاديمية، ومدير النظام، ورئيس القسم، وعميد الكلية، وعضو هيئة التدريس، والطالب. **يوضّح المخطط:** طريق الجدول من طرح المقررات وإنشاء الشعب وضبط القواعد وجمع أوقات التفرّغ، إلى بنائه واعتماده ونشره، ثم عرضه وتعديله في الطوارئ.

**العلاقات:**

- «حل التعارضات بحلول مقترحة» توسّع «بناء الجدول الدراسي آلياً وتعديله» حين تبقى في الجدول تعارضات.
- «اقتراح مدرّس بديل» توسّع «تعديل الجدول في الحالات الطارئة» حين يغيب المدرّس بإجازة معتمدة.
- يبني المنسق الجدول ويرسله للاعتماد، ويعتمده موظف الشؤون الأكاديمية وينشره، كما يعتمد قبل ذلك المقررات المطروحة.
- يتابع المنسق ورئيس القسم والعميد تسليم أوقات التفرّغ، كلٌّ في نطاقه.
- يطلب عضو هيئة التدريس الاعتذار عن محاضرة أو تعويضها، ويقبل المنسق الطلب أو يرفضه في «الرد على طلبات الاعتذار والتعويض».

![UCD-06-scheduling: الجدول الدراسي](Images/UCD-06-scheduling.png)

<div dir="ltr">

```plantuml
@startuml UCD-06-scheduling
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

actor "موظف الشؤون\nالأكاديمية" as ACO
actor "مدير النظام" as ADM
actor "منسق الجداول\nوالموارد" as CRD
actor "رئيس القسم" as HOD
actor "عميد الكلية" as DEN
actor "عضو هيئة\nالتدريس" as INS
actor "الطالب" as STU

rectangle "الجدول الدراسي\nCourse Timetabling" {
  usecase "اعتماد طرح المقررات\nوالجدول ونشره" as APPROVE
  usecase "ضبط قواعد الجدولة\nوشروطها" as RULES
  usecase "إنشاء الشعب\nوإسناد مدرّسيها" as SECTIONS
  usecase "طرح مقررات الفصل\nوتقدير أعداد طلابها" as OFFER
  usecase "بناء الجدول الدراسي\nآلياً وتعديله" as BUILD
  usecase "إرسال الجدول\nللاعتماد" as SUBMIT
  usecase "تعديل الجدول\nفي الحالات الطارئة" as EMERG
  usecase "الرد على طلبات\nالاعتذار والتعويض" as DECIDE
  usecase "متابعة تسليم أوقات التفرّغ\nوتذكير المتأخرين" as FOLLOW
  usecase "طلب اعتذار عن محاضرة\nأو تعويضها" as ABS
  usecase "إدخال أوقات التفرّغ" as AVAIL
  usecase "عرض الجدول الأسبوعي\nوتنزيله" as VIEW
  usecase "حل التعارضات\nبحلول مقترحة" as CONFL
  usecase "اقتراح مدرّس بديل" as SUBST
}

ACO -- APPROVE
ADM -- RULES
ADM -- SECTIONS
CRD -- RULES
CRD -- SECTIONS
CRD -- OFFER
CRD -- BUILD
CRD -- SUBMIT
CRD -- EMERG
CRD -- DECIDE
CRD -- FOLLOW
HOD -- FOLLOW
DEN -- FOLLOW
INS -- ABS
INS -- AVAIL
INS -- VIEW
STU -- VIEW

BUILD <.. CONFL : <<extend>>
EMERG <.. SUBST : <<extend>>
@enduml
```

</div>

---

## 07. التدريس والحضور (Teaching and Attendance)

**الفاعلون:** عضو هيئة التدريس، والطالب، وموظف الشؤون الأكاديمية، ورئيس القسم، وعميد الكلية. **يوضّح المخطط:** محتوى المادة وإعلاناتها، والاختبارات القصيرة، والحضور والغياب والحرمان، وتقييم المقررات ونتائجه.

**العلاقات:**

- يسجّل عضو هيئة التدريس الحضور يدوياً أو يعرض رمز QR، ويسجّل الطالب حضوره بمسح الرمز بجواله.
- يطّلع الطالب على غيابه وإنذاراته، ويعتمد موظف الشؤون الأكاديمية حرمان من تجاوز غيابه الحد.
- يقيّم الطالب المقرر والمدرّس دون كشف هويته، ويطّلع المدرّس ورئيس القسم والعميد على النتائج.

![UCD-07-teaching: التدريس والحضور](Images/UCD-07-teaching.png)

<div dir="ltr">

```plantuml
@startuml UCD-07-teaching
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

actor "رئيس القسم" as HOD
actor "عميد الكلية" as DEN
actor "عضو هيئة\nالتدريس" as INS
actor "الطالب" as STU
actor "موظف الشؤون\nالأكاديمية" as ACO

rectangle "التدريس والحضور\nTeaching and Attendance" {
  usecase "الاطلاع على نتائج\nتقييم المقررات" as EVALRES
  usecase "نشر محتوى المادة\nوإعلاناتها" as CONTENT
  usecase "إعداد الاختبارات\nالقصيرة ونشرها" as QUIZ
  usecase "تسجيل الحضور\n(يدوياً أو بمسح رمز QR)" as ATT
  usecase "تصفّح محتوى المادة\nوإعلاناتها" as PAGE
  usecase "أداء الاختبار القصير" as TAKE
  usecase "تقييم المقرر\nوالمدرّس" as EVAL
  usecase "عرض غيابي\nوإنذاراته" as MYABS
  usecase "اعتماد حرمان الطلاب\nبسبب الغياب" as DEPRIV
}

HOD -- EVALRES
DEN -- EVALRES
INS -- EVALRES
INS -- CONTENT
INS -- QUIZ
INS -- ATT
STU -- ATT
STU -- PAGE
STU -- TAKE
STU -- EVAL
STU -- MYABS
ACO -- DEPRIV
@enduml
```

</div>

---

## 08. الامتحانات والعلامات (Exams and Marks)

**الفاعلون:** موظف شؤون الامتحانات، وعضو هيئة التدريس، وموظف الشؤون الأكاديمية، ورئيس القسم، وعميد الكلية، والطالب. **يوضّح المخطط:** جدول الامتحانات وقاعاتها ومراقبوها، ويوم الامتحان، وطريق العلامة من إدخالها إلى نشرها وتعديلها، وما يراه الطالب.

**العلاقات:**

- «إعداد جدول الامتحانات» يتضمن «توزيع القاعات والمقاعد والمراقبين».
- كل من «مطابقة العلامات واعتمادها ونشرها» و«اعتماد تعديل علامة منشورة» يتضمن «حساب المعدّل والوضع الأكاديمي».
- طريق العلامة: يدخلها المدرّس، ثم يراجعها رئيس القسم، ثم يطابقها موظف شؤون الامتحانات ويعتمدها وينشرها.
- يطلب المدرّس تعديل علامة منشورة بسبب موثّق، فيعتمد موظف الشؤون الأكاديمية التعديل الصغير، ويعتمد العميد التعديل الكبير أو الذي يحوّل النجاح رسوباً أو العكس.
- يراقب عضو هيئة التدريس قاعة الامتحان فيسجّل حضورها وحوادثها.

![UCD-08-exams-marks: الامتحانات والعلامات](Images/UCD-08-exams-marks.png)

<div dir="ltr">

```plantuml
@startuml UCD-08-exams-marks
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

actor "موظف شؤون\nالامتحانات" as EXM
actor "عضو هيئة\nالتدريس" as INS
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "عميد الكلية" as DEN
actor "رئيس القسم" as HOD
actor "الطالب" as STU

rectangle "الامتحانات والعلامات\nExams and Marks" {
  usecase "إعداد جدول الامتحانات" as EXSCHED
  usecase "مطابقة العلامات\nواعتمادها ونشرها" as PUBLISH
  usecase "متابعة يوم الامتحان\n(الحضور والحوادث)" as EXDAY
  usecase "إدخال علامات الطلاب\nوإرسالها للمراجعة" as MARKS
  usecase "طلب تعديل علامة\nبعد نشرها" as REQCHANGE
  usecase "اعتماد تعديل\nعلامة منشورة" as APPCHANGE
  usecase "مراجعة علامات\nشُعب القسم" as REVIEW
  usecase "عرض جدول امتحاناتي\nوبطاقة الامتحان" as EXCARD
  usecase "عرض علاماتي\nومعدّلي" as GRADES
  usecase "توزيع القاعات والمقاعد\nوالمراقبين" as DIST
  usecase "حساب المعدّل\nوالوضع الأكاديمي" as GPA
}

EXM -- EXSCHED
EXM -- PUBLISH
EXM -- EXDAY
INS -- EXDAY
INS -- MARKS
INS -- REQCHANGE
ACO -- APPCHANGE
DEN -- APPCHANGE
HOD -- REVIEW
STU -- EXCARD
STU -- GRADES

EXSCHED ..> DIST : <<include>>
PUBLISH ..> GPA : <<include>>
APPCHANGE ..> GPA : <<include>>
@enduml
```

</div>

---

## 09. القبول والتسجيل (Admission and Registration)

**الفاعلون:** موظف القبول، والمتقدّم للقبول، وموظف الشؤون الأكاديمية، والطالب، وبوابة الدفع الإلكتروني. **يوضّح المخطط:** القبول من فتح دوراته إلى نشر نتائجه وتحوّل المقبول إلى طالب، ثم تسجيل المقررات والسحب والإضافة.

**العلاقات:**

- «تقديم طلب الالتحاق ومتابعته» يتضمن «دفع رسوم التقديم» عبر بوابة الدفع الإلكتروني.
- «قبول عرض القبول» يتضمن «إنشاء ملف الطالب ورقمه الجامعي»، فيصبح المتقدّم طالباً.
- كل من «تسجيل المقررات» و«السحب والإضافة» يتضمن «التحقق من أهلية التسجيل».
- «الانتظار على مقعد في شعبة ممتلئة» توسّع «تسجيل المقررات» حين تمتلئ الشعبة.

![UCD-09-admission-registration: القبول والتسجيل](Images/UCD-09-admission-registration.png)

<div dir="ltr">

```plantuml
@startuml UCD-09-admission-registration
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

actor "موظف القبول" as ADO
actor "المتقدّم للقبول" as APL
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "الطالب" as STU
actor "بوابة الدفع\nالإلكتروني" as PG

rectangle "القبول والتسجيل\nAdmission and Registration" {
  usecase "فتح دورات القبول\nوتحديد شروطها" as CYCLE
  usecase "مراجعة طلبات المتقدّمين\nومستنداتهم" as DOCS
  usecase "المفاضلة بين المتقدّمين\nونشر نتائج القبول" as RANK
  usecase "تقديم طلب الالتحاق\nومتابعته" as APPLY
  usecase "قبول عرض القبول" as ACCEPT
  usecase "فتح التسجيل ونشر\nالمقررات المتاحة" as OPEN
  usecase "منح استثناءات التسجيل\nووضع الموانع ورفعها" as EXC
  usecase "تسجيل المقررات" as REG
  usecase "السحب والإضافة" as DROP
  usecase "دفع رسوم التقديم" as PAY
  usecase "إنشاء ملف الطالب\nورقمه الجامعي" as NEWSTU
  usecase "الانتظار على مقعد\nفي شعبة ممتلئة" as WAIT
  usecase "التحقق من أهلية\nالتسجيل" as ELIG
}

ADO -- CYCLE
ADO -- DOCS
ADO -- RANK
APL -- APPLY
APL -- ACCEPT
ACO -- OPEN
ACO -- EXC
STU -- REG
STU -- DROP

APPLY ..> PAY : <<include>>
ACCEPT ..> NEWSTU : <<include>>
REG <.. WAIT : <<extend>>
REG ..> ELIG : <<include>>
DROP ..> ELIG : <<include>>

PAY -- PG
@enduml
```

</div>

---

## 10. سجلات الطلاب والإرشاد (Student Records and Advising)

**الفاعلون:** موظف القبول، ومدير النظام، وموظف الشؤون الأكاديمية، والطالب، والمرشد الأكاديمي. **يوضّح المخطط:** ملفات الطلاب، وتقدّم كل طالب في خطته، وخطة الفصل وإذن التسجيل، ومواعيد الإرشاد وملاحظاته، والإنذارات وخطر التعثّر، وكشف العلامات والتخرج.

**العلاقات:**

- يقترح النظام لكل طالب خطة لفصله، فيعدّلها الطالب ويقدّمها في «تقديم خطتي للفصل إلى المرشد»، ثم يراجعها المرشد في «مراجعة خطة الطالب ومنح إذن التسجيل» فيمنحه الإذن أو يعيدها إليه بملاحظات. ولا يسجّل الطالب مقرراته (المخطط 09) قبل هذا الإذن.
- يحدد المرشد أوقات مواعيده ويتابعها، ويحجز الطالب موعداً منها.
- «تسجيل ملاحظات الإرشاد» توسّع «مراجعة خطة الطالب ومنح إذن التسجيل» و«تحديد مواعيد الإرشاد ومتابعتها» حين يدوّن المرشد ملاحظة على ملف الطالب.
- يطّلع على «عرض ما أنجزه الطالب وما بقي من خطته» الطالب لنفسه، والمرشد لطلابه، وموظف الشؤون الأكاديمية.
- يصدر موظف الشؤون الأكاديمية كشف العلامات الرسمي، ويصدر الطالب كشفه غير الرسمي.

![UCD-10-records-advising: سجلات الطلاب والإرشاد](Images/UCD-10-records-advising.png)

<div dir="ltr">

```plantuml
@startuml UCD-10-records-advising
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

actor "مدير النظام" as ADM
actor "موظف القبول" as ADO
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "الطالب" as STU
actor "المرشد الأكاديمي" as ADV

rectangle "سجلات الطلاب والإرشاد\nStudent Records and Advising" {
  usecase "إدارة ملفات الطلاب" as RECORDS
  usecase "ترشيح الخريجين\nواعتماد دفعة التخرج" as GRAD
  usecase "إصدار كشف العلامات" as TRANSCRIPT
  usecase "عرض ما أنجزه الطالب\nوما بقي من خطته" as AUDIT
  usecase "تقديم خطتي للفصل\nإلى المرشد" as SUBMITPLAN
  usecase "حجز موعد\nمع المرشد" as BOOK
  usecase "مراجعة خطة الطالب\nومنح إذن التسجيل" as REVIEWPLAN
  usecase "تحديد مواعيد الإرشاد\nومتابعتها" as SLOTS
  usecase "متابعة الإنذارات\nالأكاديمية" as WARN
  usecase "متابعة الطلاب المعرّضين\nلخطر التعثّر" as RISK
  usecase "تسجيل ملاحظات\nالإرشاد" as NOTES
}

ADM -- RECORDS
ADO -- RECORDS
ACO -- GRAD
ACO -- TRANSCRIPT
ACO -- AUDIT
STU -- TRANSCRIPT
STU -- AUDIT
STU -- SUBMITPLAN
STU -- BOOK
ADV -- AUDIT
ADV -- REVIEWPLAN
ADV -- SLOTS
ADV -- WARN
ADV -- RISK

REVIEWPLAN <.. NOTES : <<extend>>
SLOTS <.. NOTES : <<extend>>
@enduml
```

</div>

---

## 11. المالية والطلبات الإلكترونية (Finance and E-Requests)

**الفاعلون:** الموظف المالي، والطالب، والمرشد الأكاديمي، وموظف الشؤون الأكاديمية، وموظف شؤون الامتحانات، وبوابة الدفع الإلكتروني. **يوضّح المخطط:** الرسوم والفواتير والدفع والأقساط والمنح والغرامات والاسترداد، وطلبات الطالب الإلكترونية ودراستها.

**العلاقات:**

- «دفع الفاتورة إلكترونياً» توسّع «عرض رصيدي وفواتيري» حين يختار الطالب الدفع، وتنفّذه بوابة الدفع الإلكتروني.
- يدرس الطلب الإلكتروني من يحدده نوعه: المرشد الأكاديمي أو موظف الشؤون الأكاديمية أو موظف شؤون الامتحانات (كالتظلّم والامتحان البديل).
- طلب التقسيط طلب إلكتروني يبتّ فيه الموظف المالي ضمن «إدارة الأقساط والمنح والغرامات والاسترداد».

![UCD-11-finance-requests: المالية والطلبات الإلكترونية](Images/UCD-11-finance-requests.png)

<div dir="ltr">

```plantuml
@startuml UCD-11-finance-requests
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

actor "الموظف المالي" as FIN
actor "الطالب" as STU
actor "المرشد الأكاديمي" as ADV
actor "موظف الشؤون\nالأكاديمية" as ACO
actor "موظف شؤون\nالامتحانات" as EXM
actor "بوابة الدفع\nالإلكتروني" as PG

rectangle "المالية والطلبات الإلكترونية\nFinance and E-Requests" {
  usecase "إدارة الرسوم\nوالفواتير" as FEES
  usecase "تسجيل دفعة نقدية\nفي الصندوق" as CASH
  usecase "إدارة الأقساط والمنح\nوالغرامات والاسترداد" as AID
  usecase "عرض رصيدي\nوفواتيري" as BAL
  usecase "تقديم طلب إلكتروني\nومتابعته" as REQ
  usecase "دراسة الطلبات الإلكترونية\nوالرد عليها" as PROC
  usecase "دفع الفاتورة\nإلكترونياً" as PAY
}

FIN -- FEES
FIN -- CASH
FIN -- AID
STU -- BAL
STU -- REQ
ADV -- PROC
ACO -- PROC
EXM -- PROC

BAL <.. PAY : <<extend>>
PAY -- PG
@enduml
```

</div>

---

## 12. المكتبة وشؤون الموظفين (Library and Staff Affairs)

**الفاعلون:** الطالب، والموظف، وعضو هيئة التدريس، وأمين المكتبة، والمدير المباشر، وموظف شؤون الموظفين، وجهاز البصمة. **يوضّح المخطط:** البحث في المكتبة وحجز الكتب وإعارتها وغرامات التأخير، والخدمة الذاتية للموظف وإجازاته وملفاته ودوامه.

**العلاقات:**

- عضو هيئة التدريس نوع من «الموظف» (تعميم)، فيرث عرض ملفه وطلب الإجازة والبحث في المكتبة.
- «حجز نسخة معارة» توسّع «البحث عن كتاب في المكتبة» حين تكون النسخ كلها معارة.
- «احتساب غرامة التأخير» توسّع «إعارة الكتب واستلامها» حين يتأخر إرجاع الكتاب.
- يوافق المدير المباشر على الإجازة أولاً، ثم يعتمدها موظف شؤون الموظفين.
- يرسل جهاز البصمة الحضور والانصراف، ويطّلع عليهما الموظف في «عرض ملفي الوظيفي ودوامي».

![UCD-12-library-hr: المكتبة وشؤون الموظفين](Images/UCD-12-library-hr.png)

<div dir="ltr">

```plantuml
@startuml UCD-12-library-hr
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

actor "عضو هيئة\nالتدريس" as INS
actor "الموظف" as EMP
actor "الطالب" as STU
actor "أمين المكتبة" as LIB
actor "المدير المباشر" as MGR
actor "موظف شؤون\nالموظفين" as HRO
actor "جهاز البصمة" as BIO

rectangle "المكتبة وشؤون الموظفين\nLibrary and Staff Affairs" {
  usecase "عرض ملفي الوظيفي\nودوامي" as SELF
  usecase "تقديم طلب إجازة" as LEAVE
  usecase "البحث عن كتاب\nفي المكتبة" as SEARCH
  usecase "إعارة الكتب\nواستلامها" as LOAN
  usecase "الموافقة على\nطلبات الإجازة" as APPROVE
  usecase "إدارة ملفات الموظفين\nوعقودهم" as FILES
  usecase "تسجيل الحضور والانصراف\nمن جهاز البصمة" as ATTEND
  usecase "حجز نسخة معارة" as HOLD
  usecase "احتساب غرامة\nالتأخير" as FINE
}

INS -|> EMP

EMP -- SELF
EMP -- LEAVE
EMP -- SEARCH
STU -- SEARCH
LIB -- LOAN
MGR -- APPROVE
HRO -- APPROVE
HRO -- FILES

SEARCH <.. HOLD : <<extend>>
LOAN <.. FINE : <<extend>>
ATTEND --- BIO
@enduml
```

</div>

---

## 13. التقارير والذكاء الاصطناعي (Reports and AI)

**الفاعلون:** موظف الشؤون الأكاديمية، ومدير النظام، والإدارة العليا، ومنسق الجداول والموارد، وعضو هيئة التدريس، ومزوّد الذكاء الاصطناعي. **يوضّح المخطط:** تقارير الإدارة وملخصاتها، وتجربة الاحتمالات المستقبلية، وخدمات الذكاء الاصطناعي: لوائح الجامعة للمساعد الذكي، واستخراج المقررات من ملف، وتوقّع أعداد الطلاب، وشرح الجدول، وكتابة التفرّغ والشروط بجملة عادية.

**العلاقات:**

- في «رفع لوائح الجامعة ليجيب منها المساعد الذكي» يرفع موظف الشؤون الأكاديمية ملفات اللوائح، فيجيب المساعد الذكي (المخطط 01) منها ويذكر المادة التي استند إليها.
- يُعرض «توقّع أعداد الطلاب في كل مقرر» للمنسق عند طرح المقررات (المخطط 06). وفي «مقارنة دقة التوقّعات واعتماد الأفضل» يقارن مدير النظام دقة النسخة الجديدة بالحالية، ويعتمد موظف الشؤون الأكاديمية تفعيل الأدق.
- يشارك مزوّد الذكاء الاصطناعي في الحالات التي تحتاج إلى فهم نص أو كتابته؛ أما التوقّع ومقارنة الدقة وتجربة الاحتمالات فيحسبها النظام بنفسه.
- ومن خدمات الذكاء الاصطناعي أيضاً: سؤال المساعد الذكي (المخطط 01)، ومتابعة الطلاب المعرّضين لخطر التعثّر (المخطط 10).

![UCD-13-reports-ai: التقارير والذكاء الاصطناعي](Images/UCD-13-reports-ai.png)

<div dir="ltr">

```plantuml
@startuml UCD-13-reports-ai
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

actor "موظف الشؤون\nالأكاديمية" as ACO
actor "مدير النظام" as ADM
actor "الإدارة العليا" as EXE
actor "منسق الجداول\nوالموارد" as CRD
actor "عضو هيئة\nالتدريس" as INS
actor "مزوّد الذكاء\nالاصطناعي" as LLM

rectangle "التقارير والذكاء الاصطناعي\nReports and AI" {
  usecase "رفع لوائح الجامعة ليجيب\nمنها المساعد الذكي" as KB
  usecase "استخراج المقررات\nمن ملف PDF" as EXTRACT
  usecase "مقارنة دقة التوقّعات\nواعتماد الأفضل" as MODEL
  usecase "ضبط خدمة الذكاء\nالاصطناعي وحدودها" as AISET
  usecase "طلب ملخص للتقرير\nبالذكاء الاصطناعي" as SUMMARY
  usecase "عرض التقارير\nولوحات المؤشرات" as REPORTS
  usecase "تجربة احتمالات\nمستقبلية (ماذا لو؟)" as SIM
  usecase "توقّع أعداد الطلاب\nفي كل مقرر" as FORECAST
  usecase "شرح سبب وضع\nالمحاضرات في أوقاتها" as EXPLAIN
  usecase "كتابة التفرّغ والشروط\nبجملة عادية" as NL
}

ACO -- KB
ACO -- EXTRACT
ACO -- MODEL
ADM -- MODEL
ADM -- AISET
ADM -- SUMMARY
ADM -- REPORTS
EXE -- SUMMARY
EXE -- REPORTS
EXE -- SIM
CRD -- SIM
CRD -- FORECAST
CRD -- EXPLAIN
CRD -- NL
INS -- EXPLAIN
INS -- NL

KB --- LLM
EXTRACT --- LLM
SUMMARY --- LLM
EXPLAIN --- LLM
NL --- LLM
@enduml
```

</div>

---

## ملاحظات

- **ما ليس فاعلاً:** ما هو جزء من النظام نفسه، كمحرك الجدولة والمساعد الذكي ونماذج التوقّع ونظام الإشعارات.
- **من يُربط بالحالة:** من ينفّذها أو يتخذ فيها قراراً أو يطّلع بها على ما يخصه. أما من يُبلَّغ بنتيجتها فقط فلا يُربط بها، لأن الإشعار يصله في «متابعة الإشعارات».
- **تسمية الحالة:** تُسمّى كل حالة بما يفعله الفاعلون المرتبطون بها. فإن قام شخصان بجزأين مختلفين من عمل واحد، كتقديم طلب والبت فيه، رُسمت لكل منهما حالة باسم عمله، مثل «تقديم خطتي للفصل إلى المرشد» للطالب و«مراجعة خطة الطالب ومنح إذن التسجيل» للمرشد.
- **مدير النظام:** يظهر في المخططات 03 و04 و05 و06 و10 لأن سيناريوهاتها تمنحه صلاحية المسؤول نفسه: الفصول، وسلالم التقدير، والقاعات والأجهزة، والشعب وقواعد الجدولة، وملفات الطلاب.
- **ما ليس حالة استخدام:** النتائج (كالقبول والرفض) والخطوات الداخلية (كمتابعة تقدّم التوليد) ليست أهدافاً للفاعل. أما الفحوص والحسابات التي تتكرر في أكثر من حالة، مثل «التحقق من أهلية التسجيل» و«حساب المعدّل والوضع الأكاديمي»، فتظهر حالاتٍ مضمَّنة.

</div>
