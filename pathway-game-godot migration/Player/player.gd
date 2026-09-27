@tool
extends CharacterBody2D


@export var speed = 300.0
var screen_size = get_viewport_rect().size



func _ready():
	screen_size = get_viewport_rect().size
	
func _process(delta):
	
	if Input.is_action_pressed("move_right"):
		velocity.x +=1
	if Input.is_action_pressed("move_left"):
		velocity.x -=1
	if Input.is_action_pressed("move_up"):
		velocity.y -=1
	if Input.is_action_pressed("move_down"):
		velocity.y +=1
		
	if velocity.length() >0:
		velocity = velocity.normalized() * speed
		$AnimatedSprite2D.play() # $ is get node
	else:
		$AnimatedSprite2D.stop()
	move_and_slide()
	
	position += velocity * delta
	
	position.x = clamp(position.x,0,screen_size.x)
	position.y = clamp(position.y,0,screen_size.y)

	
