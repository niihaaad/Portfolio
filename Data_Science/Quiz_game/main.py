import pygame
import time
from quiz import Quiz
from questions_loader import load_questions

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 48)

clock = pygame.time.Clock()

# Charger les questions
questions = load_questions()
quiz = Quiz(questions)


# --------------------------------------------------------
#  BOUTONS
# --------------------------------------------------------
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, surface, color=(220, 220, 220)):
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        text_surf = font.render(self.text, True,  (0,0,0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)


# --------------------------------------------------------
#  SCREENS (MENU - QUIZ - GAME OVER)
# --------------------------------------------------------

def menu_screen():
    start_button = Button("Commencer le jeu", 250, 300, 300, 70)

    while True:
        screen.fill((255, 255, 255))

        title = big_font.render("QUIZ GAME", True, (0, 0, 0))
        screen.blit(title, (280, 150))

        start_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_hovered(pygame.mouse.get_pos()):
                    return "play"

        pygame.display.flip()
        clock.tick(60)


def draw_question():
    q = quiz.get_current_question()

    # Afficher score en haut
    score_text = font.render(f"Score : {quiz.score}", True,  (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # Afficher la question
    question_text = font.render(q.question, True,  (255, 255, 255))
    screen.blit(question_text, (20, 80))

    # Générer boutons de réponses
    buttons = []
    start_y = 180

    for i, choice in enumerate(q.choices):
        btn = Button(choice, 80, start_y + i * 80, 640, 60)
        btn.draw(screen)
        buttons.append(btn)

    return buttons


def game_over_screen():
    replay_button = Button("Rejouer", 250, 350, 300, 70)

    while True:
        screen.fill((255, 255, 255))

        title = big_font.render("Fin du Quiz !", True, (0, 0, 0))
        score_text = font.render(f"Score final : {quiz.score}", True,  (255, 255, 255))

        screen.blit(title, (260, 150))
        screen.blit(score_text, (310, 250))

        replay_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.is_hovered(pygame.mouse.get_pos()):
                    return "restart"

        pygame.display.flip()
        clock.tick(60)


# --------------------------------------------------------
#  MAIN GAME LOOP
# --------------------------------------------------------

def game_loop():
    global quiz
    quiz = Quiz(load_questions())  # reset quiz data at start

    while True:
        screen.fill((30, 30, 60))

        buttons = draw_question()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for i, btn in enumerate(buttons):
                    if btn.is_hovered(pos):

                        # Vérifier réponse
                        correct = quiz.check_answer(i)

                        # Couleur verte ou rouge
                        color = (0, 255, 0) if correct else (255, 0, 0)
                        btn.draw(screen, color)
                        pygame.display.flip()
                        time.sleep(0.7)  # petite pause visuelle

                        # Question suivante ou fin
                        if not quiz.next_question():
                            return "game_over"

        pygame.display.flip()
        clock.tick(60)


# --------------------------------------------------------
#  PROGRAM FLOW (MENU → QUIZ → FIN)
# --------------------------------------------------------
while True:
    action = menu_screen()
    if action == "quit":
        break

    action = game_loop()
    if action == "quit":
        break

    action = game_over_screen()
    if action == "restart":
        continue
    else:
        break

pygame.quit()
