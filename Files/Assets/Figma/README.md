# OptiTime UI design in Figma

**The file:** https://www.figma.com/design/fGwkfL9BoQ9oe72FGUkrAz
(named "OptiTime — UI Design").

The screens follow the implemented site's design: the same colors, sidebar, cards, and Cairo font. They weren't taken from screenshots. Every screen is drawn as editable layers and built from components. The colors, fonts, shadows, and motion values come from `Code/optitime-frontend/src/assets/tokens.css`.

## What's in the file

| Page | Contents |
|---|---|
| 00 · Cover & Foundations | The cover, plus a foundations board: color, radius, and spacing variables, `motion/*` variables, 11 Cairo text styles, 7 shadows, and a Motion section (durations and easing curves) |
| 01 · Components | 108 Bootstrap Icons. Interactive components with an animated Hover state: Button, IconButton, NavItem, NavGroup, SubNavItem. Components that change inside the prototype: Toggle (flips on click) and NotificationRow (becomes read on click). Content components: Badge, Avatar, SidebarBrand, UserCard, SearchField, Topbar, StatCard, Lecture, Field, SectionHeader |
| 02 · Screens & Prototype | A prototype guide, 36 screens, and 11 states/overlays (listed below) |

| # | Screen | Role |
|---|---|---|
| 01 | Login | Everyone |
| 02 | Dashboard | Senior management |
| 03 | Timetable Studio | Schedule and resource coordinator |
| 04 | My weekly timetable | Faculty member |
| 05 | Course management | System administrator |
| 06 | User management | System administrator |
| 07 | Room management | System administrator |
| 08 | Management reports | Senior management |
| 09 · 10 | Login and dashboard on a phone | — |
| 11 | The studio after auto-fix (prototype state) | Schedule coordinator |
| 12 | "New course" popup | System administrator |
| 13 | Notifications list | Everyone |
| 14 | Mobile slide-out menu | — |
| 15 | Academic Calendar (October 2026 month view, events, upcoming, legend) | Senior management |
| 16 | Notifications Centre (clickable notifications) | Senior management |
| 17 | User Settings (profile, security, devices, notifications, appearance, advanced) | Senior management |
| 18 | Notifications Centre after "Mark all as read" (prototype state) | Senior management |
| 19 | Calendar event details popup | Senior management |

### Faculty member and student screens

These cover the whole faculty member and student experience. Several are modules the app hasn't built yet (quizzes, attendance, gradebook, finance, registration, careers, e-requests). They follow the SRS features 4.47–4.79 and use the same components and colours as the built pages. Persona: د. ريم العلي (faculty member) and نور الحسن (third-year Informatics student, from the proposal). "Today" is Tuesday 20 October 2026, week 7 of 20.

| # | Screen | Role |
|---|---|---|
| 20 | Dashboard: next lecture, today, tasks, sections, students near the absence limit, AI at-risk note | Faculty member |
| 21 | Course page (CS113): syllabus progress, files, announcements | Faculty member |
| 22 | Attendance: roster with present/late/absent/excused, rotating QR code | Faculty member |
| 23 | Quizzes and question banks: quiz list, banks by question type, AI question suggestions, score spread | Faculty member |
| 24 | Gradebook: one mark out of 100 from weighted parts, approval chain, unusual-mark warning | Faculty member |
| 25 | Employment self-service: leave with its effect on teaching, attendance log, contract, load, evaluation (no salary, per REQ-HRM-02) | Faculty member |
| 26 | Availability: one sentence turned into rules by the assistant, weekly grid | Faculty member |
| 27 | Teaching profile: qualified courses, preferences, degrees | Faculty member |
| 28 | Lecture requests: apology and make-up with slots the engine suggests | Faculty member |
| 29 | Resource requests: status, reasons, comments | Faculty member |
| 30 | Room bookings: own bookings and a free-room finder | Faculty member |
| 31 | "New quiz" popup: timing, attempts, shuffling, extra time for one student, questions from a bank | Faculty member |
| 32 | Attendance QR code shown full screen | Faculty member |
| 40 | Dashboard: next lecture, today, quiz open now, latest marks, assistant, attendance | Student |
| 41 | Weekly timetable with a room-change notice | Student |
| 42 | My grades: one compact row per subject that opens on its parts | Student |
| 43 | Quizzes: open now, coming up, results | Student |
| 44 | Taking a quiz (full-screen mode): timer, question, question map | Student |
| 45 | Exams: timetable, seat map, exam card with QR, eligibility | Student |
| 46 | Study plan and degree audit: requirement groups, plan map, prerequisites, advisor | Student |
| 47 | Course registration: eligibility checklist, live seats, cart, week preview, every rule checked at once | Student |
| 48 | Transcript: A4 preview with a verification code, term GPAs | Student |
| 49 | Finance: invoice, instalments, account ledger, scholarship, refund table | Student |
| 50 | Internships and jobs: openings ranked by fit with the reason, applications, CV completeness | Student |
| 51 | E-requests: request types with their promised time, my requests, approval timeline | Student |
| 52 | Pay an instalment (popup) | Student |
| 53 | AI assistant panel: an answer with its sources | Student |
| 54 | Quiz submitted (result) | Student |

Screen 04 now uses the full faculty sidebar (الرئيسية, مساحتي with شؤوني الوظيفية, and the new التدريس group) and the same October week.

## LinkedIn post

The **00** page (below the cover) holds a frame named `LinkedIn Post — OptiTime (1080×1350)`. It's a portrait post at LinkedIn's ideal size, showing the real Timetable Studio screen in a browser window, the phone dashboard, and real performance figures (2,952 lectures across 370 rooms in about 20 seconds, with zero hard conflicts).
To export it: select the frame, then **Export** at the bottom of the right panel, choose **PNG** at **2x**, and click **Export**.

## Running the prototype

Open the **02** page, then press ▶ **Present** and pick a scenario from **Flows**:

1. **Senior management:** login → dashboard ↔ management reports.
2. **Schedule coordinator:** "Auto-fix all" → the fixed state. "Undo the fix" goes back.
3. **System administrator:** move between courses, users, and rooms from the sidebar groups. "New course" opens a popup.
4. **Faculty member:** the weekly timetable.
5. **Phone:** login → dashboard. The menu button slides the menu out from the right.
6. **Senior management, Calendar, Notifications, and Settings:** every item in the senior management sidebar now works: dashboard ↔ calendar ↔ notifications ↔ reports ↔ settings.
7. **Faculty member (20):** every page in مساحتي and التدريس opens from the sidebar; a closed group opens its first page. The dashboard's next lecture, tasks and section cards open their pages. "Show QR" in attendance opens 32. "New quiz" or "Continue editing" opens 31.
8. **Student (40):** every page in دراستي, الشؤون الأكاديمية and خدماتي opens from the sidebar. Start quiz → 44 → Submit → 54 → back to quizzes or try again. The assistant question (dashboard or the refund table) opens 53, whose "Start a withdrawal" opens e-requests. "Pay now" in finance opens 52.

In the faculty and student sidebars, الإشعارات opens the notifications list (13). The calendar and settings items aren't linked, since those pages (15, 17) are the same for every role.

Inside the new screens:
- **Calendar:** clicking the "quiz week" bar, or its card in "قادم" (upcoming), opens the event details (19).
- **Notifications:** clicking an unread notification marks it read. "Mark all as read" leads to state 18, and "Undo" in the toast brings them back. "Notification settings" opens Settings.
- **Settings:** each sidebar sub-menu item (profile, security, two-step verification, devices, notifications, appearance, advanced) scrolls smoothly to its section, and the switches flip when clicked.
- "View all notifications" in the bell dropdown opens the Notifications Centre.

On every desktop screen, the bell opens the notifications list and the logout icon returns to the login screen. Clicking outside a popup closes it.

## Transition system (from the site's motion tokens)

| Interaction | Transition | Duration | Easing |
|---|---|---|---|
| Hover on buttons and sidebar items | Smart Animate | 160ms (`--ot-d-fast`) | `--ot-ease` 0.4, 0, 0.2, 1 |
| Popups and menus | Dissolve / Move in | 280ms (`--ot-d-base`) | `--ot-ease-out` 0.16, 1, 0.3, 1 |
| Moving between pages | Smart Animate (the sidebar stays put, the content moves) | 520ms (`--ot-d-slow`) | `--ot-ease-out` |
| Login | Dissolve | 520ms | `--ot-ease-out` |
| A state change within the same page (marking as read) | Smart Animate | 280ms | `--ot-ease-out` |
| Settings sub-menu → section | Scroll Animate | 520ms | `--ot-ease-out` |
| Switches, and a notification turning read | Smart Animate | 160ms | `--ot-ease` |

## Exported images (in this folder)

Every design is also saved here as a PNG at 2x, sorted by role:

| Folder | Contents |
|---|---|
| `00 الغلاف والأساسيات - Cover & Foundations` | Cover, foundations board, LinkedIn post |
| `01 المكوّنات - Components` | Icons and the three component boards |
| `02 مشتركة - Shared` | 01 login, 13 notifications list |
| `03 الجوال - Mobile` | 09, 10, 14 |
| `04 الإدارة العليا - Senior Management` | 02, 08, 15–19 |
| `05 منسق الجدولة - Schedule Coordinator` | 03, 11 |
| `06 مدير النظام - System Administrator` | 05–07, 12 |
| `07 عضو هيئة التدريس - Teacher` | 04, 20–32 |
| `08 الطالب - Student` | 40–54 |
| `09 دليل النموذج التفاعلي - Prototype Guide` | The prototype guide |

Popups (12, 13, 14, 19, 31, 52, 53) are saved over the screen they open from, as they appear in the prototype. For that, the Screens page has seven frames named `Export · …` below the states row. They can be deleted once the images are saved.

Every frame in the file has a "PNG 2x" export preset. To export again: open a page, select everything (Ctrl+A), and click **Export** at the bottom of the right panel. Figma downloads a ZIP. Then run `python -I _tools/sort_exports.py` to put the newest `OptiTime*.zip` from Downloads into these folders (`--dry` lists what it would do). A ZIP that includes the `Export · …` frames also carries copies of their base screens cut to the popup's height. For that ZIP, pass `--only=40-54` (the range you're adding), so those copies don't replace the full screens; the composites are always taken. A bare popup never replaces a saved popup-over-screen image.

## Notes

- The data in the screens is realistic sample data. The current database has no published timetable yet.
- The free Starter plan allows only 3 pages per file.
- To edit: change a component on the Components page and every screen updates. Colors live in **Variables** (OptiTime Tokens).
- To share with the supervisor: click **Share**, then add her email or copy the link with "can view" permission.
