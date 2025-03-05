-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2025 at 10:28 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kmmgwc`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add employee', 7, 'add_employee'),
(26, 'Can change employee', 7, 'change_employee'),
(27, 'Can delete employee', 7, 'delete_employee'),
(28, 'Can view employee', 7, 'view_employee'),
(29, 'Can add event', 8, 'add_event'),
(30, 'Can change event', 8, 'change_event'),
(31, 'Can delete event', 8, 'delete_event'),
(32, 'Can view event', 8, 'view_event'),
(33, 'Can add news', 9, 'add_news'),
(34, 'Can change news', 9, 'change_news'),
(35, 'Can delete news', 9, 'delete_news'),
(36, 'Can view news', 9, 'view_news'),
(37, 'Can add notification', 10, 'add_notification'),
(38, 'Can change notification', 10, 'change_notification'),
(39, 'Can delete notification', 10, 'delete_notification'),
(40, 'Can view notification', 10, 'view_notification'),
(41, 'Can add news image', 11, 'add_newsimage'),
(42, 'Can change news image', 11, 'change_newsimage'),
(43, 'Can delete news image', 11, 'delete_newsimage'),
(44, 'Can view news image', 11, 'view_newsimage');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$4Scq2BccsUtNwRk52wFk01$csKIh0FHuwEAzmZrXN/ex/85P9nXoBddm2mckt3Zw8o=', '2025-02-14 05:41:07.346665', 1, 'snclg@vdk', '', '', 'sncvatakara@gmail.com', 1, 1, '2024-01-08 16:31:06.574232');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'employee'),
(8, 'myapp', 'event'),
(9, 'myapp', 'news'),
(11, 'myapp', 'newsimage'),
(10, 'myapp', 'notification'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-01-08 15:36:48.806255'),
(2, 'auth', '0001_initial', '2024-01-08 15:36:50.322274'),
(3, 'admin', '0001_initial', '2024-01-08 15:36:50.761001'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-01-08 15:36:50.786792'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-01-08 15:36:50.808519'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-01-08 15:36:51.016211'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-01-08 15:36:51.203745'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-01-08 15:36:51.465093'),
(9, 'auth', '0004_alter_user_username_opts', '2024-01-08 15:36:51.496554'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-01-08 15:36:51.657089'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-01-08 15:36:51.675618'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-01-08 15:36:51.705459'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-01-08 15:36:51.878515'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-01-08 15:36:52.077234'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-01-08 15:36:52.268362'),
(16, 'auth', '0011_update_proxy_permissions', '2024-01-08 15:36:52.288941'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-01-08 15:36:52.536414'),
(18, 'myapp', '0001_initial', '2024-01-08 15:36:52.617555'),
(19, 'myapp', '0002_event', '2024-01-08 15:36:52.663247'),
(20, 'myapp', '0003_news', '2024-01-08 15:36:52.710397'),
(21, 'myapp', '0004_remove_news_photos_newsimage', '2024-01-08 15:36:53.065191'),
(22, 'myapp', '0005_notification', '2024-01-08 15:36:53.205062'),
(23, 'myapp', '0006_employee_department', '2024-01-08 15:36:53.308420'),
(24, 'myapp', '0007_news_date', '2024-01-08 15:36:53.411510'),
(25, 'myapp', '0008_news_image_delete_newsimage', '2024-01-08 15:36:53.529456'),
(26, 'myapp', '0009_newsimage', '2024-01-08 15:36:53.737242'),
(27, 'sessions', '0001_initial', '2024-01-08 15:36:53.906981');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0moic5mq3kl6x4ys07h3oxeof5uv7wi8', 'eyJ1c2VybmFtZSI6IlNuY2xnQHZkayAifQ:1rphAd:UNcI3BXljkO9r83boRWHbT8Txhhx0gUvff-ZfvMqfLA', '2024-04-11 04:15:19.159883'),
('3uelf8r4u3akbhy4z6co6a5m00nnm45o', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rdVeG:Hb9BLQOQW5608l8Zm7ksH1Fda6_Do5pCk__PpwluULI', '2024-03-08 13:31:32.382870'),
('3unfv7jd0o4m80le0kqmgsgscddevbfk', 'eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sjC8N:gg2IdNsy3_W_U7rhEivos6zGB3m_n6XXSIxravw6vUc', '2024-09-11 06:26:23.484449'),
('al03rlqx1gc5epq7bkr5kpb8wjnm9wap', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rx0Y4:9JRSPJFklBmhmXkesNvY39SIX0cMVRTF0Mg0bAmFUpw', '2024-05-01 08:21:44.990553'),
('azjd51dgjpgizaiahz4uhxrq86mnu9oq', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sOvwx:mVqAu59onoCzRCMhz7s3YASSA-yV1gpxsruXx3VlZHM', '2024-07-17 09:06:51.839871'),
('c3arw6ukt3zl790n6j76n6yia0nf7wcg', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rNUAS:l4yckvrd-cABIdrWojr_UHVHkmdczjc14EJIvNvWa6o', '2024-01-24 08:42:32.387955'),
('g0lyhmaxo8y182kxsz0auy0fpdymg66y', 'eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sdNh1:a6kNjAJ5ael873WoAWE6mRanpPecAIVAkOhiftOWG1s', '2024-08-26 05:34:07.031121'),
('gjd0elhalf3eyhl5pnyz6vxt5qfn13po', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sSGRj:VrOSWmyeeYJfT_GBHWC2ly3ovNgLsyoY5DgdzthBW0M', '2024-07-26 13:36:23.994116'),
('hqgxveg16i0pa09ia6be3cvzylfi5y1o', '.eJxVzEsOgjAYBOC7dG2alhZaXBn2noH8j_IQLAkFN8a7SxMWupvMTL63aGHfhnZPYW1HFlehxeW3Q6ApxDzwA2K_SFrito4o80Wea5L3hcPcnN8_YIA0ZFaXukBVOKOscwS-rIK1daEQCfEIoTPeM9fOY-mM1mArw6YjUjU6UgeauQjPcGgp0tzfXjyJzxcIlz8h:1tYfTo:PLPk05nAkTyvEcugK5PXX-E-8F6N8Fp_AHIhr99OSec', '2025-01-31 06:05:16.719076'),
('iyzogve7v83pir3by2yimywdz34f5ucx', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sA9WO:gFizY4S9X4BKfplLugsLRn-kPvoLAhZJN4cnE-HgtI4', '2024-06-06 14:34:20.454969'),
('kieg4qkhv4xz28crtczqo40wf8n6t5by', '.eJxVjMsOwiAQRf-FtSE8C7h07zcQZoZK1UBS2pXx35WkC93d3HNyXiymfStx73mNC7Ezk-z0-0HCR64D0D3VW-PY6rYuwIfCD9r5tVF-Xg73L1BSLyMrrVQglNPCOIfJ2ykbE5QAQIDvyLP2nig4D9ZpKZOZNOkZUQRwKNj7A7doNzc:1tioRn:TngcQb46sJQILM5PdlNUgb4cq7U8jtaFe2R4_0_I6JA', '2025-02-28 05:41:07.353734'),
('kkmi2k9rxx3vbmmc83hl7n290j0xfzru', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rVxIe:ZgeJuNjqF2f0AA6FfUQUbcfBLwLDlVUlAT4I4QQYpZA', '2024-02-16 17:26:00.784928'),
('l7twwbyt5p9d5savj70uugnpe7yx32l3', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rSeKt:gkZ8PnI45A3TjBpz3Uvd4wnfWKpVDuFq3GO-klfA3ss', '2024-02-07 14:34:39.775653'),
('lb4hpmp926m6jb0pmm2i8uh7xjbufu7e', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rQPMD:sKojkNl7ba-RqzFe4hcCK6vQLtwFoscLbF1X22e83dk', '2024-02-01 10:10:45.114206'),
('oltczsjc4bczcnk6yrhleuk1ac271i1l', 'eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sM2eB:FcjO5dVOQEjJNFY8G9jQWzqP59o92rWT96zKvkF0MOQ', '2024-07-09 09:39:31.364984'),
('psv1fmafijeyfsx586dl49e0xv18s3mb', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1sSGRj:VrOSWmyeeYJfT_GBHWC2ly3ovNgLsyoY5DgdzthBW0M', '2024-07-26 13:36:23.238813'),
('pwxfvu0lnpvjmd8i804p2wbgaq1nfelq', 'eyJ1c2VybmFtZSI6IlNuY2xnQHZkayJ9:1sEsLr:eA2WtkUgHKCRjQUx8ImI7eWm1BdzKlAz_YD9SXUtqbQ', '2024-06-19 15:14:59.606101'),
('qtpvbta5eyzfmtzkf0qedkbcolgrq5a7', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rfDnz:ckDkLQ-rGWK_HSUfUhUtkD9XeBolnuWozKhygB5do50', '2024-03-13 06:52:39.127644'),
('rigq5oofzqzmwvggkyscl4vv0hbr4sw6', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1s9M68:aBrMiwSGlCYHU8zR7zh4PEtsw3VhcsmQhnoAxHIXwWs', '2024-06-04 09:47:56.493559'),
('skr0pjcu5x4hd2o4s3zvyoupjaahmaav', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rcgKW:lF8hgr3enevP2DGAvBLz9fKrzplog6kz_CTRggtaiTI', '2024-03-06 06:43:44.007883'),
('z5zobsgx27i6i8sj6v94tfppti44od1v', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rPfRS:t1WH1qpvXisbnHkIbhNEDhjUg1t-D_Y60r4wKWWapy8', '2024-01-30 09:09:06.877660'),
('zihya9222sqvgpjuu09b9pm4799gcs31', 'eyJ1c2VybmFtZSI6InNuY2xnQHZkayJ9:1rSBLC:tlZDzARHd2uoOxR1giNq4qvobUBiv00mAy_2WpgpIkQ', '2024-02-06 07:37:02.415073');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_employee`
--

CREATE TABLE `myapp_employee` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `position` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `qualification` longtext NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_employee`
--

INSERT INTO `myapp_employee` (`id`, `name`, `position`, `photo`, `qualification`, `department`) VALUES
(3, 'PAVITHRAN M T', 'Assistant Professor', 'photos/DSC01444.JPG', 'MCA , PGDCA', 'COMPUTER SCIENCE'),
(4, 'VYSAKH O K', 'Head Of Department', 'photos/vys.jpg', 'MCA ,PGDCA', 'COMPUTER APPLICATION'),
(6, 'ABHIRAM KRISHNA A', 'Assistant Professor', 'photos/Screenshot_20240109_122852-01.jpeg', 'MSc Computer Science, NET', 'COMPUTER APPLICATION');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_event`
--

CREATE TABLE `myapp_event` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `time` time(6) NOT NULL,
  `date` date NOT NULL,
  `description` longtext NOT NULL,
  `venue` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_event`
--

INSERT INTO `myapp_event` (`id`, `title`, `time`, `date`, `description`, `venue`, `url`) VALUES
(2, 'WEBSITE LAUNCHING CEREMONY', '10:00:00.000000', '2024-01-18', 'College website Inauguration Ceremony', 'Seminar Hall', ''),
(20, 'വിജ്ഞാനോത്സവം- FYUGP 2024', '10:00:00.000000', '2024-07-01', 'വിജ്ഞാനോത്സവം- FYUGP 2024 programme conducted by Kerala state Government.\r\nState Level Inauguration : Honorable Chief Minister Sri. PINARAYI VIJAYAN\r\nCollege Level Inauguration : Sri. T ASHRAF (Maniyur Gramapanchayat President)', 'Seminar Hall', ''),
(23, ' ARTS DAY', '11:37:00.000000', '2025-01-25', 'Krishna Menon Memorial Government Women’s College  ARTS DAY', 'seminar hall', '');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_news`
--

CREATE TABLE `myapp_news` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `date` date NOT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_news`
--

INSERT INTO `myapp_news` (`id`, `title`, `description`, `date`, `image`) VALUES
(18, 'Convocation Ceremony : Department of Psychology ', 'Convocation Ceremony of 2021-23 PG students had conducted by Department of Psychology.', '2023-10-25', ''),
(19, 'Shuttle Badminton Championship ', 'Shuttle Badminton Championship inaugurated by College Principal Dr. M K Radhakrishnan & conducted by Department of Physical Education on 23rd February 2024 at college campus.', '2024-02-23', ''),
(32, '\"ചേർത്ത് നിർത്താം പ്രകൃതിയെ നല്ലൊരു നാളെയ്ക്കുവേണ്ടി ', 'ജൂൺ 5 പരിസ്ഥിതിദിനത്തോടനുബന്ധിച്ചു എൻ എസ് എസ് വോളന്റീർസ് കോളേജ് അംഗണത്തിൽ വൃക്ഷതൈകൾ നട്ടുപിടിപ്പിച്ചു', '2024-06-05', '');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_newsimage`
--

CREATE TABLE `myapp_newsimage` (
  `id` bigint(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `news_article_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_newsimage`
--

INSERT INTO `myapp_newsimage` (`id`, `image`, `news_article_id`) VALUES
(35, 'news_images/IMG-20240223-WA0038_4RXt2Ml.jpg', 18),
(36, 'news_images/IMG-20240223-WA0037_c5aSwWn.jpg', 18),
(37, 'news_images/IMG-20240223-WA0021.jpg', 19),
(38, 'news_images/IMG-20240223-WA0031.jpg', 19),
(76, 'news_images/greek.jpg', 32),
(77, 'news_images/1560675_424328394366171_308053817_n.jpg', 32),
(78, 'news_images/WhatsApp_Image_2024-03-09_at_5.jpg', 32),
(79, 'news_images/pexels-stijn-dijkstra-2659475.jpg', 32);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_notification`
--

CREATE TABLE `myapp_notification` (
  `id` bigint(20) NOT NULL,
  `category` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `file` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `myapp_notification`
--

INSERT INTO `myapp_notification` (`id`, `category`, `title`, `description`, `file`) VALUES
(3, 'ug', '1st Semester UG Examination has been postponed to March 4th 2024', '1st Semester UG Examination has been postponed to March 4th 2024', 'uploads/2024-02-03_16_19_51_exnot7900.pdf'),
(4, 'ug', 'Calicut University Student Portal Registration 2023 admission onwards ', '          All students who took admission 2023 onwards should register Calicut university Students portal. Registration instruction are attached here.', 'uploads/STUDENT_PORTAL_REGISTRATION.pdf'),
(10, 'ug', 'FYUGP Major & Minor Courses', 'We offered the 13 Major Disciplines under Calicut University', 'uploads/IMG-20240523-WA00361.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_employee`
--
ALTER TABLE `myapp_employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_event`
--
ALTER TABLE `myapp_event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_news`
--
ALTER TABLE `myapp_news`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_newsimage`
--
ALTER TABLE `myapp_newsimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_newsimage_news_article_id_87547bc6_fk_myapp_news_id` (`news_article_id`);

--
-- Indexes for table `myapp_notification`
--
ALTER TABLE `myapp_notification`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `myapp_employee`
--
ALTER TABLE `myapp_employee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;

--
-- AUTO_INCREMENT for table `myapp_event`
--
ALTER TABLE `myapp_event`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `myapp_news`
--
ALTER TABLE `myapp_news`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `myapp_newsimage`
--
ALTER TABLE `myapp_newsimage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `myapp_notification`
--
ALTER TABLE `myapp_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_newsimage`
--
ALTER TABLE `myapp_newsimage`
  ADD CONSTRAINT `myapp_newsimage_news_article_id_87547bc6_fk_myapp_news_id` FOREIGN KEY (`news_article_id`) REFERENCES `myapp_news` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
