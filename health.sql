--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Homebrew)
-- Dumped by pg_dump version 14.8 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.users DROP CONSTRAINT users_condition_id_fkey;
ALTER TABLE ONLY public.favorites DROP CONSTRAINT favorites_user_id_fkey;
ALTER TABLE ONLY public.favorites DROP CONSTRAINT favorites_recipe_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.recipes DROP CONSTRAINT recipes_pkey;
ALTER TABLE ONLY public.health_conditions DROP CONSTRAINT health_conditions_pkey;
ALTER TABLE ONLY public.favorites DROP CONSTRAINT favorites_pkey;
ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
ALTER TABLE public.recipes ALTER COLUMN recipe_id DROP DEFAULT;
ALTER TABLE public.health_conditions ALTER COLUMN condition_id DROP DEFAULT;
ALTER TABLE public.favorites ALTER COLUMN favorite_id DROP DEFAULT;
DROP SEQUENCE public.users_user_id_seq;
DROP TABLE public.users;
DROP SEQUENCE public.recipes_recipe_id_seq;
DROP TABLE public.recipes;
DROP SEQUENCE public.health_conditions_condition_id_seq;
DROP TABLE public.health_conditions;
DROP SEQUENCE public.favorites_favorite_id_seq;
DROP TABLE public.favorites;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: favorites; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.favorites (
    favorite_id integer NOT NULL,
    user_id integer NOT NULL,
    recipe_id integer NOT NULL
);


--
-- Name: favorites_favorite_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.favorites_favorite_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: favorites_favorite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.favorites_favorite_id_seq OWNED BY public.favorites.favorite_id;


--
-- Name: health_conditions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.health_conditions (
    condition_id integer NOT NULL,
    condition_name character varying(50) NOT NULL,
    condition_description character varying NOT NULL,
    min_carbs integer,
    max_carbs integer,
    "min_Cholesterol" integer,
    "max_Cholesterol" integer,
    "min_SaturatedFat" integer,
    "max_SaturatedFat" integer,
    "min_Sugar" integer,
    "max_Sugar" integer,
    "min_Iron" integer
);


--
-- Name: health_conditions_condition_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.health_conditions_condition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: health_conditions_condition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.health_conditions_condition_id_seq OWNED BY public.health_conditions.condition_id;


--
-- Name: recipes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.recipes (
    recipe_id integer NOT NULL,
    title character varying,
    image character varying,
    source_url character varying
);


--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.recipes_recipe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.recipes_recipe_id_seq OWNED BY public.recipes.recipe_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(25) NOT NULL,
    password character varying NOT NULL,
    condition_id integer
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: favorites favorite_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.favorites ALTER COLUMN favorite_id SET DEFAULT nextval('public.favorites_favorite_id_seq'::regclass);


--
-- Name: health_conditions condition_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.health_conditions ALTER COLUMN condition_id SET DEFAULT nextval('public.health_conditions_condition_id_seq'::regclass);


--
-- Name: recipes recipe_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.recipes ALTER COLUMN recipe_id SET DEFAULT nextval('public.recipes_recipe_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: favorites; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.favorites (favorite_id, user_id, recipe_id) FROM stdin;
1	3	715415
2	4	716426
3	4	716627
4	5	642892
5	5	1697533
6	6	782585
7	6	715497
8	6	641128
9	6	664147
10	6	715497
29	8	715497
30	8	715497
116	10	782601
117	10	644387
118	10	716627
119	10	716627
61	8	715497
62	8	715497
63	8	715497
64	8	640941
\.


--
-- Data for Name: health_conditions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.health_conditions (condition_id, condition_name, condition_description, min_carbs, max_carbs, "min_Cholesterol", "max_Cholesterol", "min_SaturatedFat", "max_SaturatedFat", "min_Sugar", "max_Sugar", "min_Iron") FROM stdin;
1	hypertension	Hypertension, commonly known as high blood pressure, is a chronic medical condition characterized by persistently elevated blood pressure levels in the arteries.	0	0	0	70	0	5	0	0	0
2	diabetes	Diabetes is a chronic metabolic disorder characterized by high blood sugar levels, resulting from inadequate insulin production or impaired insulin function. Insulin, produced by the pancreas, regulates the absorption and utilization of glucose in the body. In type 1 diabetes, the immune system mistakenly attacks and destroys the insulin-producing cells in the pancreas, while in type 2 diabetes, the body becomes resistant to insulin or doesn't produce enough of it. Diabetes can lead to various complications affecting the eyes, kidneys, nerves, and cardiovascular system. It requires lifelong management, including blood sugar monitoring, healthy eating, regular physical activity, and, in some cases, medication or insulin therapy under the guidance of healthcare professionals.	0	50	0	60	0	5	0	10	0
3	heart_health	Heart disease refers to a range of conditions that affect the heart's structure and function. It is often used interchangeably with the term cardiovascular disease, which encompasses various conditions affecting the blood vessels as well. Heart diseases can include coronary artery disease, heart failure, arrhythmias, and valvular heart disease. These conditions can result from factors like high blood pressure, high cholesterol, smoking, obesity, and a sedentary lifestyle. Prevention and management of heart disease involve lifestyle modifications, including a heart-healthy diet, regular exercise, avoidance of smoking, and appropriate medical interventions under the care of healthcare professionals.	0	0	0	70	0	5	0	0	0
4	anemia	Anemia is a medical condition characterized by a decrease in the number of red blood cells or a decrease in the amount of hemoglobin within the red blood cells. Hemoglobin is responsible for carrying oxygen to tissues throughout the body. Anemia can result from various factors, including nutritional deficiencies (such as iron, vitamin B12, or folate), chronic diseases, inherited disorders, or blood loss. Treatment for anemia depends on the underlying cause and may involve dietary changes, supplements, medications, or other interventions recommended by a healthcare professional.	0	0	0	0	0	0	0	0	15
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.recipes (recipe_id, title, image, source_url) FROM stdin;
715497	Berry Banana Breakfast Smoothie	https://spoonacular.com/recipeImages/715497-556x370.jpg	\N
715415	Red Lentil Soup with Chicken and Turnips	https://spoonacular.com/recipeImages/715415-556x370.jpg	\N
716426	Cauliflower, Brown Rice, and Vegetable Fried Rice	https://spoonacular.com/recipeImages/716426-556x370.jpg	\N
716627	Easy Homemade Rice and Beans	https://spoonacular.com/recipeImages/716627-556x370.jpg	\N
642892	Fire Roasted Tomato Chutney	https://spoonacular.com/recipeImages/642892-556x370.jpg	\N
1697533	Roasted Tomato and White Bean Stew	https://spoonacular.com/recipeImages/1697533-556x370.jpg	\N
782585	Cannellini Bean and Asparagus Salad with Mushrooms	https://spoonacular.com/recipeImages/782585-556x370.jpg	\N
641128	Curry Mussels	https://spoonacular.com/recipeImages/641128-556x370.jpg	\N
664147	Tuscan White Bean Soup with Olive Oil and Rosemary	https://spoonacular.com/recipeImages/664147-556x370.jpg	\N
795751	Chicken Fajita Stuffed Bell Pepper	https://spoonacular.com/recipeImages/795751-556x370.jpg	\N
644387	Garlicky Kale	https://spoonacular.com/recipeImages/644387-556x370.jpg	\N
663108	Thai Fish Cakes	https://spoonacular.com/recipeImages/663108-556x370.jpg	\N
640941	Crunchy Brussels Sprouts Side Dish	https://spoonacular.com/recipeImages/640941-556x370.jpg	\N
715446	Slow Cooker Beef Stew	https://spoonacular.com/recipeImages/715446-556x370.jpg	\N
638166	Chicken Liver Salad	https://spoonacular.com/recipeImages/638166-556x370.jpg	\N
716406	Asparagus and Pea Soup: Real Convenience Food	https://spoonacular.com/recipeImages/716406-556x370.jpg	\N
766453	Hummus and Za'atar	https://spoonacular.com/recipeImages/766453-556x370.jpg	\N
715495	Turkey Tomato Cheese Pizza	https://spoonacular.com/recipeImages/715495-556x370.jpg	\N
782601	Red Kidney Bean Jambalaya	https://spoonacular.com/recipeImages/782601-556x370.jpg	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (user_id, username, password, condition_id) FROM stdin;
1	techwizzz	techwizzz2023	\N
2	programmer2023	programmer!!!	\N
3	itsmeagain2023	itsmeagain2023	\N
4	drue	drue	\N
5	2024isclose	2024isclose	\N
6	julybabies	julybaby1990	\N
7	SulNRosh	sulnrosh2023	\N
8	July2023	July*2023	\N
9	suliman2023	Suliman2023	\N
10	ghandabadi	ghandabadi2023	\N
11	roshisme	roshisme2023	\N
12	roshd	roshd2023	\N
\.


--
-- Name: favorites_favorite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.favorites_favorite_id_seq', 122, true);


--
-- Name: health_conditions_condition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.health_conditions_condition_id_seq', 4, true);


--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.recipes_recipe_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 12, true);


--
-- Name: favorites favorites_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_pkey PRIMARY KEY (favorite_id);


--
-- Name: health_conditions health_conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.health_conditions
    ADD CONSTRAINT health_conditions_pkey PRIMARY KEY (condition_id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: favorites favorites_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id);


--
-- Name: favorites favorites_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: users users_condition_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_condition_id_fkey FOREIGN KEY (condition_id) REFERENCES public.health_conditions(condition_id);


--
-- PostgreSQL database dump complete
--

