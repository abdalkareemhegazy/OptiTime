# OptiTime UI design in Figma

**The file:** https://www.figma.com/design/fGwkfL9BoQ9oe72FGUkrAz
(named "OptiTime — UI Design").

The screens follow the implemented site's design: the same colors, sidebar, cards, and Cairo font. They weren't taken from screenshots. Every screen is drawn as editable layers and built from components. The colors, fonts, shadows, and motion values come from `Code/optitime-frontend/src/assets/tokens.css`.

## What's in the file

| Page | Contents |
|---|---|
| 00 · Cover & Foundations | The cover, plus a foundations board: color, radius, and spacing variables, `motion/*` variables, 11 Cairo text styles, 7 shadows, and a Motion section (durations and easing curves) |
| 01 · Components | 69 Bootstrap Icons. Interactive components with an animated Hover state: Button, IconButton, NavItem, NavGroup, SubNavItem. Components that change inside the prototype: Toggle (flips on click) and NotificationRow (becomes read on click). Content components: Badge, Avatar, SidebarBrand, UserCard, SearchField, Topbar, StatCard, Lecture, Field, SectionHeader |
| 02 · Screens & Prototype | A prototype guide, 13 screens, and 6 states/overlays (listed below) |

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

## Notes

- The data in the screens is realistic sample data. The current database has no published timetable yet.
- The free Starter plan allows only 3 pages per file.
- To edit: change a component on the Components page and every screen updates. Colors live in **Variables** (OptiTime Tokens).
- To share with the supervisor: click **Share**, then add her email or copy the link with "can view" permission.
