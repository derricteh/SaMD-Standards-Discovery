{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "baafd5cf-7170-4be9-95af-d8dcfe3f6545",
   "metadata": {},
   "source": [
    "# Secret key \n",
    "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"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "313d14d3-dd10-4e4f-9a2f-0f5b0a88d8e8",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openai in c:\\users\\user\\anaconda3\\lib\\site-packages (2.8.1)Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "wsproto 1.3.2 requires h11<1,>=0.16.0, but you have h11 0.14.0 which is incompatible.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (4.2.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (0.26.0)\n",
      "Requirement already satisfied: jiter<1,>=0.10.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (0.12.0)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (2.5.3)\n",
      "Requirement already satisfied: sniffio in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (1.3.0)\n",
      "Requirement already satisfied: tqdm>4 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (4.66.4)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in c:\\users\\user\\anaconda3\\lib\\site-packages (from openai) (4.15.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\user\\anaconda3\\lib\\site-packages (from anyio<5,>=3.5.0->openai) (3.7)\n",
      "Requirement already satisfied: certifi in c:\\users\\user\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->openai) (2025.10.5)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\user\\anaconda3\\lib\\site-packages (from httpx<1,>=0.23.0->openai) (1.0.2)\n",
      "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->openai)\n",
      "  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pydantic<3,>=1.9.0->openai) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.14.6 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pydantic<3,>=1.9.0->openai) (2.14.6)\n",
      "Requirement already satisfied: colorama in c:\\users\\user\\anaconda3\\lib\\site-packages (from tqdm>4->openai) (0.4.6)\n",
      "Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
      "   ---------------------------------------- 0.0/58.3 kB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/58.3 kB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/58.3 kB ? eta -:--:--\n",
      "   ------- -------------------------------- 10.2/58.3 kB ? eta -:--:--\n",
      "   ----------------------------------- ---- 51.2/58.3 kB 525.1 kB/s eta 0:00:01\n",
      "   ---------------------------------------- 58.3/58.3 kB 510.8 kB/s eta 0:00:00\n",
      "Installing collected packages: h11\n",
      "  Attempting uninstall: h11\n",
      "    Found existing installation: h11 0.16.0\n",
      "    Uninstalling h11-0.16.0:\n",
      "      Successfully uninstalled h11-0.16.0\n",
      "Successfully installed h11-0.14.0\n"
     ]
    }
   ],
   "source": [
    "# installation of libraries\n",
    "# pip install openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "24be470b-6935-4b19-b801-636406d60b86",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setting up API token in environment\n",
    "import os\n",
    "os.environ['OPENAI_API_KEY'] = \"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\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "07217bad-f2a1-4ae5-88cf-0841f47988f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Under the silver moon, a gentle unicorn trotted through a field of starlight, curled up by the sleepy brook, and drifted into dreamland as the night whispered a lullaby.\n"
     ]
    }
   ],
   "source": [
    "from openai import OpenAI\n",
    "client = OpenAI()\n",
    "\n",
    "response = client.responses.create(\n",
    "    model=\"gpt-5-nano\",\n",
    "    input=\"Write a one-sentence bedtime story about a unicorn.\"\n",
    ")\n",
    "\n",
    "print(response.output_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "128d21e6-b9a6-4064-af17-d4229332cd1b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d813928a-eaf8-450b-ae09-2b31221a86ca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
