output "image_id" {
  description = "ID of the nginx image"
  value       = docker_image.nginx.image_id
}

output "container_id" {
  description = "ID of the nginx container"
  value       = docker_container.nginx.id  # Inconsistent, should be `.container_id`
}
