from manim import *
import numpy as np

class MainScene(Scene):
    def construct(self):
        # Title
        title = Text("4x4 Matrix Exponentiation", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Create 4x4 matrix A
        matrix_a = Matrix([
            ["1", "2", "0", "1"],
            ["0", "1", "1", "0"],
            ["1", "0", "1", "2"],
            ["0", "1", "0", "1"]
        ], left_bracket="[", right_bracket="]").scale(0.6)
        
        a_label = Text("A = ", font_size=28).next_to(matrix_a, LEFT)
        matrix_group = VGroup(a_label, matrix_a).move_to([-3, 0.5, 0])
        
        self.play(Write(a_label), Create(matrix_a))
        self.wait()
        
        # Show exponentiation concept
        exp_text = Text("Matrix Exponentiation: A^n", font_size=28).move_to([2.5, 1.5, 0])
        self.play(Write(exp_text))
        
        # Show A^2 = A * A
        a_squared = Text("A^2 = A x A", font_size=24).move_to([2.5, 0.5, 0])
        self.play(Write(a_squared))
        
        # Result matrix for A^2
        result_matrix = Matrix([
            ["2", "5", "2", "3"],
            ["1", "1", "2", "2"],
            ["2", "4", "1", "5"],
            ["0", "2", "1", "1"]
        ], left_bracket="[", right_bracket="]").scale(0.5)
        
        result_label = Text("A^2 = ", font_size=24).next_to(result_matrix, LEFT)
        result_group = VGroup(result_label, result_matrix).move_to([2.5, -1.2, 0])
        
        self.play(Write(result_label), Create(result_matrix))
        
        # Show formula for matrix exponentiation
        formula = Text("A^n = A x A x ... x A (n times)", font_size=22)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        # Highlight applications
        apps_title = Text("Applications:", font_size=24, color=YELLOW).move_to([-3, -1.5, 0])
        app1 = Text("- Graph path counting", font_size=20).move_to([-3, -2, 0])
        app2 = Text("- Fibonacci numbers", font_size=20).move_to([-3, -2.5, 0])
        
        self.play(Write(apps_title))
        self.play(Write(app1), Write(app2))
        
        self.wait(2)